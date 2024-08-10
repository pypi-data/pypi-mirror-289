import argparse
import asyncio
from pathlib import Path

from PIL import Image
from hypy_utils import printc, json_stringify, write
from hypy_utils.dict_utils import remove_keys
from pyrogram import Client
from pyrogram.file_id import FileId
from pyrogram.types import User, Chat, Message, Sticker

from .config import load_config, Config
from .consts import HTML
from .convert import convert_text, convert_media_dict
from .download_media import download_media, has_media, guess_ext, download_media_urlsafe
from .grouper import group_msgs
from ..convert_export import remove_nones
from ..convert_media_types import tgs_to_apng
from ..rss.posts_to_feed import posts_to_feed, FeedMeta


def effective_text(msg: Message) -> str:
    """
    Get effective text of a message in HTML
    """
    if msg.text:
        return convert_text(msg.text, msg.text.entities)
    if msg.caption:
        return convert_text(msg.caption, msg.caption.entities)
    if msg.service:
        return str(msg.service).split(".")[-1].replace("_", " ").capitalize()


def _download_media_helper(args: list) -> Path:
    return asyncio.run(download_media(app, *args))


def get_user_name(user: User) -> str:
    name = user.first_name or ""
    if user.last_name:
        name += " " + user.last_name
    return name


async def process_message(msg: Message, path: Path, export: dict) -> dict:
    media_path = path / "media"

    m = {
        "id": msg.id,
        "date": msg.date,
        "type": 'service' if msg.service else None,
        "text": effective_text(msg),
        "author": msg.author_signature,
        "views": msg.views,
        "forwards": msg.forwards,
        "forwarded_from": {
            "name": get_user_name(msg.forward_from),
            "url": f'https://t.me/{msg.forward_from.username}' if msg.forward_from.username else None,
        } if msg.forward_from else {
            "name": msg.forward_from_chat.title,
        } if msg.forward_from_chat else {
            "name": msg.forward_sender_name,
        } if msg.forward_sender_name else None,
        "media_group_id": msg.media_group_id,
        "reply_id": msg.reply_to_message_id,
        "file": convert_media_dict(msg)
    }

    # Download file
    f = m.get('file')

    async def dl_media():
        fp, name = await download_media_urlsafe(app, msg, directory=media_path,
                                                max_file_size=int((export.get('size_limit_mb') or 0) * 1000_000))
        if fp is None:
            return
        f['original_name'] = name

        # Convert tgs sticker
        if fp.suffix == '.tgs':
            fp = Path(tgs_to_apng(fp))

        f['url'] = str(fp.absolute().relative_to(path.absolute()))
        f['size'] = f.pop('file_size', None)

        # Download the largest thumbnail
        if f.get('thumbs'):
            thumb: dict = max(f['thumbs'], key=lambda x: x['file_size'])
            ext = guess_ext(app, FileId.decode(thumb['file_id']).file_type, None)
            fp = await download_media(app, thumb['file_id'], directory=media_path,
                                      fname=fp.with_suffix(fp.suffix + f'_thumb{ext}').name)
            f['thumb'] = str(fp.absolute().relative_to(path.absolute()))
            del f['thumbs']

    if has_media(msg):
        await dl_media()

    # Move photo to its own key
    if f:
        mt = f.get('media_type')
        if mt == 'photo' or (not mt and (f.get('mime_type') or "").startswith("image")):
            img = m['image'] = m.pop('file')

            # Read image size
            img['width'], img['height'] = Image.open(path / img['url']).size

    return remove_keys(remove_nones(m), {'file_id', 'file_unique_id'})


async def download_custom_emojis(msgs: list[Message], results: list[dict], path: Path):
    print("Downloading custom emojis...")
    # List custom emoji ids
    ids = {e.custom_emoji_id for msg in msgs if msg.text and msg.text.entities for e in msg.text.entities if e.custom_emoji_id}
    ids.update({e.custom_emoji_id for msg in msgs if msg.caption_entities for e in msg.caption_entities if e.custom_emoji_id})
    ids = list(ids)
    orig_ids = list(ids)

    # Query stickers 200 ids at a time
    stickers: list[Sticker] = []
    while ids:
        stickers += await app.get_custom_emoji_stickers(ids[:200])
        ids = ids[200:]

    # Download stickers
    for id, s in zip(orig_ids, stickers):
        ext = guess_ext(app, FileId.decode(s.file_id).file_type, s.mime_type)
        op = (await download_media(app, s, path / "emoji", f'{id}{ext}')).absolute().relative_to(path.absolute())

        # Replace sticker paths
        for r in results:
            if "text" in r:
                r['text'] = r['text'].replace(f'<i class="custom-emoji" emoji-src="emoji/{id}">',
                                              f'<i class="custom-emoji" emoji-src="{op}">')


async def process_chat(chat_id: int, path: Path, export: dict):
    chat: Chat = await app.get_chat(chat_id)
    printc(f"&aChat obtained. Chat name: {chat.title} | Type: {chat.type} | ID: {chat.id}")

    # Crawl 200 messages each request
    print("Crawling channel posts...")
    msgs = []
    for i in range(999):
        start_idx = i * 200 + 1
        end_idx = start_idx + 200

        additional_msgs = await app.get_messages(chat.id, range(start_idx, end_idx))
        additional_msgs = [m for m in additional_msgs if not m.empty]
        msgs += additional_msgs
        print(f"> {len(msgs)} total messages... (up to ID #{end_idx - 1})")

        if not additional_msgs:
            print("> All 200 messages are empty, we're done.")
            break

    # print(msgs)
    results = [await process_message(m, path, export) for m in msgs]
    await download_custom_emojis(msgs, results, path)

    # Group messages
    results = group_msgs(results)

    write(path / "posts.json", json_stringify(results, indent=2))
    write(path / "index.html", HTML.replace("$$POSTS_DATA$$", json_stringify(results)))

    if 'rss' in export:
        print("Exporting RSS feed...")
        posts_to_feed(path, FeedMeta(**export['rss']))

    printc(f"&aDone! Saved to {path / 'posts.json'}")


async def run_app():
    me: User = await app.get_me()
    printc(f"&aLogin success! ID: {me.id} | is_bot: {me.is_bot}")
    for export in cfg.exports:
        await process_chat(int(export["chat_id"]), Path(export["path"]), export)


cfg: Config
app: Client


def run():
    global app, cfg
    parser = argparse.ArgumentParser("Telegram Channel Message to Public API Crawler")
    parser.add_argument("config", help="Config path", nargs="?", default="config.toml")
    args = parser.parse_args()
    cfg = load_config(args.config)

    app = Client("Bot", cfg.api_id or 2048, cfg.api_hash or "b18441a1ff607e10a989891a5462e627",
                 **(dict(bot_token=cfg.bot_token) if cfg.bot_token else {}))

    with app:
        asyncio.get_event_loop().run_until_complete(run_app())
