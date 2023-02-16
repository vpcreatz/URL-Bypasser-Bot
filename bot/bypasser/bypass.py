from bot import app, logger
from pyrogram import filters
import PyBypass as bypasser


@app.on_message(filters.command('bypass'))
async def bypass(_, msg):
    nam = None
    m = msg.text.split()
    
    if len(m)<2:
        await msg.reply_text("Format: /bypass <url> <name only if required>", parse_mode="markdown")
        return
    if len(m)>2:
        nam = m[2]
        
    url = m[1]
    x = await msg.reply_text(f"Trying to Bypass __`{url}`__...")

    try:
        if nam!=None:
            bypassed = bypasser.bypass(url, name=nam)
        bypassed = bypasser.bypass(url)
    except Exception as e:
        await x.delete()
        await msg.reply_text(f"Couldn't bypass {url}\nError: {e}")
        return

    await x.delete()
    await msg.reply_text(f"**BYPASSED URL:** `{bypassed}`")


@app.on_message(filters.command('gdtot'))
async def gdtotbypass(_, msg):
    m = msg.text.split()
    
    if len(m)<3:
        await msg.reply_text("Format: /bypass <url> <gdtot crypt>", parse_mode="markdown")
        return
    
    url = m[1]
    crypt = m[2]
    
    x = await msg.reply_text(f"Trying to Bypass __`{url}`__...")
    
    try:
        bypassed = bypasser.bypass(url, gdtot_crypt=crypt)
    except Exception as e:
        await x.delete()
        await msg.reply_text(f"Couldn't bypass {url}\nError: {e}")
        return

    await x.delete()
    await msg.reply_text(f"**BYPASSED URL:** `{bypassed}`")
    return
