import os
from bot import app
from pyrogram import filters



@app.on_message(filters.command('rename'))
async def rename(_, message):
    if not message.reply_to_message:
        await message.reply("Please reply to a file/document")
    try:
        filename = message.text.replace(message.text.split(" ")[0], "")
    except Exception as e:
        print(e)
    reply = message.reply_to_message
    if reply:
        x = await message.reply_text("Downloading.....")
        path = await reply.download(file_name=filename)
        await x.edit("Uploading.....")
        await message.reply_document(path)
        os.remove(path)



@app.on_message(filters.command("tgupload"))
async def tgupload(_, msg):
    if msg.reply_to_message:
        address = msg.reply_to_message.text
        
    else:
        try:
            address = msg.text.split()[1]
        except:
            return await msg.reply_text("Please Reply to a Url")
    
    x = await msg.reply_text("Uploading to telegram...")
    try:
        if address.startswith("http"):
            if address.endswith((".jpg", ".png", ".jpeg")):
                await msg.reply_photo(address)
                await msg.reply_document(address)
            elif address.endswith((".mp4", ".mkv", ".mov")):
                if len(msg)>2:
                    await msg.reply_document(address)
                else:
                    await msg.reply_video(address)
            else:
                await msg.reply_document(address)
        else:
            if True:
                await msg.reply_document(address)
        await x.delete()
    except:
        await msg.reply("No such File/Directory/Link")
        return
