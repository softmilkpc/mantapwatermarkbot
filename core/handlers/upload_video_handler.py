import time
from humanfriendly import format_timespan
from configs import Config
from core.display_progress import progress_for_pyrogram, humanbytes
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_video_handler(bot, cmd, output_vid, video_thumbnail, duration, width, height, editable, file_size):
    c_time = time.time()
    sent_vid = await bot.send_video(
        chat_id=cmd.chat.id,
        video=output_vid,
        caption=f"**Channel:** `{Config.CAPTION}`\n\n**Video Duration:** `{format_timespan(duration)}`\n**File Size:** `{humanbytes(file_size)}`\n",
        thumb=video_thumbnail,
        duration=duration,
        width=width,
        height=height,
        reply_to_message_id=cmd.message_id,
        supports_streaming=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/mantapvids")],
                                           [InlineKeyboardButton("Group Video", url="https://ouo.io/qjnTY6")],
                                           [InlineKeyboardButton("Group Gratis", url="https://t.me/groupgratis")]]),
        progress=progress_for_pyrogram,
        progress_args=(
            "Lagi ngupload, sabar cok !!!",
            editable,
            c_time
        )
    )
    return sent_vid
