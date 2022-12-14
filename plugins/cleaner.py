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
        await message.reply_text("โ **๐๐๐ฅ๐๐ญ๐๐ ๐๐ฅ๐ฅ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ ๐๐ข๐ฅ๐๐ฌ**")
    else:
        await message.reply_text("โ **๐๐จ ๐๐ข๐ฅ๐๐ฌ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("โ **๐๐๐ฅ๐๐ญ๐๐ ๐๐ฅ๐ฅ ๐๐๐ฐ ๐๐ข๐ฅ๐๐ฌ**")
    else:
        await message.reply_text("โ **๐๐จ ๐๐๐ฐ ๐๐ข๐ฅ๐๐ฌ**")


@Client.on_message(command(["cl", "cleanup"]) & ~filters.edited)
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("โ **ฦ๐ฅาฝ๐ษณาฝิ**")
    else:
        await message.reply_text("โ **ฮ๐ฅ๐ซ๐๐๐๐ฒ ฦ๐ฅ๐๐๐ง๐๐**")
