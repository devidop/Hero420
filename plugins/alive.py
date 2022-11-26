import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from config import GROUP_SUPPORT, OWNER_NAME, UPDATES_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("/start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/c3c80222ce8b0e6f033bc.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🥀 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐀𝐦 𝐋𝐢𝐩𝐬𝐡𝐚 𝐌𝐮𝐬𝐢𝐜 📀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝
𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐕𝐂 𝐏𝐥𝐚𝐲𝐞𝐫 » 𝐅𝐨𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦
𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐀𝐧𝐝 𝐆𝐫𝐨𝐮𝐩𝐬 ✨ ...

💐 𝐅𝐞𝐞𝐥 𝐅𝐫𝐞𝐞 𝐓𝐨: 🕊️ 𝐀𝐝𝐝 𝐌𝐞 𝐢𝐧 𝐘𝐨𝐮𝐫
𝐆𝐫𝐨𝐮𝐩 🌺 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 🌿 𝐒𝐮𝐩𝐞𝐫 𝐇𝐢𝐠𝐡
𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 🌷 ...
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ 𝐒ᴜᴘᴇʀ Ғᴀ𝐬ᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞](https://t.me/kattar_hindu_rudra)
┣★ ᴜᴘᴅᴀᴛᴇ𝐒 : [𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞](https://t.me/love_ka_funda)
┣★ 𝐒ᴜᴘᴘᴏʀᴛ : [𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞](https://t.me/about_devil30)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇ𝐒ᴛɪᴏɴ𝐒 ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/purnu) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦋 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗦𝗲𝗿𝘃𝗲𝗿 🦋", url=f"https://t.me/love_ka_funda")
                ]
                
           ]
        ),
    )
    
