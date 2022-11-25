import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["/clean", "rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐀𝐥𝐥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐅𝐢𝐥𝐞𝐬**")
    else:
        await message.reply_text("❌ **𝐍𝐨 𝐅𝐢𝐥𝐞𝐬 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐀𝐥𝐥 𝐑𝐚𝐰 𝐅𝐢𝐥𝐞𝐬**")
    else:
        await message.reply_text("❌ **𝐍𝐨 𝐑𝐚𝐰 𝐅𝐢𝐥𝐞𝐬**")


@Client.on_message(command(["cl", "cleanup"]) & ~filters.edited)
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **Ƈ𝐥ҽ𝐚ɳҽԃ**")
    else:
        await message.reply_text("✅ **Α𝐥𝐫𝐞𝐚𝐝𝐲 Ƈ𝐥𝐞𝐚𝐧𝐞𝐝**")
