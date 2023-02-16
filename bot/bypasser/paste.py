import requests
from bot import app, logger
from pyrogram import filters

SUPPORTED_FILE_TYPES = [".html", ".txt", ".log"]

def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = requests.post(url, data={"content": text, "extension": "txt"})
    if res.status_code>200:
        return f"https://spaceb.in/{res.json()['payload']['id']}"
    else:
        logger.warning("Getting low status code/\Func: paste")
        return
    

@app.on_message(filters.command('paste'))
async def pastewo(_, msg):
    status_msg = await msg.reply_text("Processing...")
    reply = msg.reply_to_message
    
    if reply:
        if reply.text:
            text = msg.reply_to_message.text
        if reply.document and (reply.document.file_size<(10 * 1024**2)):
            # any(file_name.endswith(s) for s in SUPPORTED_FILE_TYPES)
            
            try:
                path = await reply.download()
                with open(path) as data:
                    text = data.read()
                    
            except Exception as e:
                logger.error(e, "caused by FUNC: pasteowo")
                await msg.reply(f"Sorry some error excured\nERROR: {e}")
                return
            
    else:
        m = msg.text.split()
        if len(m)<2:
            await msg.reply_text("Format: /paste <reply_to_msg/text>", parse_mode="markdown")
        text = m[1]
    
    try:
        pasted = paste(text)
    except Exception as e:
        await msg.reply_text(f"Some error occurred, probably API down.\nERROR: {e}")
        logger.error(e)
        return
        
    await msg.reply_text(f"Pasted to **Spacebin**: `{pasted}`")
    await status_msg.delete()
    return 
