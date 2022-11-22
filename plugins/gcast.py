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
        wtf = await message.reply("`🌺𝗥𝗼𝘆𝗮𝗹 𝗦𝗲𝗿𝘃𝗲𝗿 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁🌺 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__ 🌺𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗧𝗼 𝗖𝗵𝗮𝘁𝘀🌺...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`🚀Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`🚀Ɠƈɑst Sʋƈƈɘssfʋɭɭy` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} Ƈɦɑts")
