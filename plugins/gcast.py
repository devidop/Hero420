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
        wtf = await message.reply("`๐บ ๐ฅ๐ผ๐๐ฎ๐น ๐ฆ๐ฒ๐ฟ๐๐ฒ๐ฟ ๐ฆ๐๐ฎ๐ฟ๐๐ถ๐ป๐ด ๐๐ฟ๐ผ๐ฎ๐ฑ๐ฐ๐ฎ๐๐ ๐บ ...`")
        if not message.reply_to_message:
            await wtf.edit("**__ ๐บ ๐ฆ๐๐ฐ๐ฐ๐ฒ๐๐๐ณ๐๐น ๐๐ฟ๐ผ๐ฎ๐ฑ๐ฐ๐ฎ๐๐ ๐บ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`๐ ฦษครธ๐ษฦ๐๐ฌ๐ญษฉลส ๐` \n\n**:** `{sent}` ฦษฆ๐๐ญ๐ฌ \n**๐๐ษฉษญษษ ๐ล:** {failed} ฦ๐ก๐๐ญ๐ฌ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`๐ ๐ฦ๐๐ฌ๐ญ ๐สฦฦษ๐ฌ๐ฌ๐สษญษญ๐ฒ ๐` \n\n**๐ษล๐ญ ฦฌรธ:** `{sent}` ฦ๐ก๐๐ญ๐ฌ \n**๐๐ษฉษญษษ ๐ล:** {failed} ฦษฆ๐๐ญ๐ฌ")
