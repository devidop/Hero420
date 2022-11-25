import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import user as aditya
from config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`🌺 𝗥𝗼𝘆𝗮𝗹 𝗦𝗲𝗿𝘃𝗲𝗿 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 🌺 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__ 🌺 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 🌺...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`🚀 Ɓɤø𝐚ɗƈ𝐚𝐬𝐭ɩŋʛ 🚀` \n\n**:** `{sent}` Ƈɦ𝐚𝐭𝐬 \n**𝐅𝐚ɩɭɘɗ 𝐈ŋ:** {failed} Ƈ𝐡𝐚𝐭𝐬")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`🚀 𝐆ƈ𝐚𝐬𝐭 𝐒ʋƈƈɘ𝐬𝐬𝐟ʋɭɭ𝐲 🚀` \n\n**𝐒ɘŋ𝐭 Ƭø:** `{sent}` Ƈ𝐡𝐚𝐭𝐬 \n**𝐅𝐚ɩɭɘɗ 𝐈ŋ:** {failed} Ƈɦ𝐚𝐭𝐬")
