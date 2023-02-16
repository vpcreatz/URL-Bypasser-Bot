from bot import app, SUPPORT_CHAT
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton as Ikb, InlineKeyboardMarkup as Ikm

mrkup=Ikm([
                [Ikb(text="📞Support", url="t.me/vp_supportgroup"), Ikb(text="⚙️Supported Link", url="https://telegra.ph/Supported-Website-Links-10-31")],
                [Ikb(text="How It Works", url="https://github.com/sanjit-sinha/PyBypass/")]
             ])

@app.on_message(filters.command(["start", "help"]))
async def start(_, message):
    text = f"**Hi! {message.from_user.first_name}**\n\n**I am a Simple url[\u200b](https://telegra.ph/Uj-10-31) bypasser bot**\n\n**Just Send me a link and I'll bypass it for you!**"
    await message.reply_text(text, reply_markup=mrkup)



def alive():
    app.run()
    app.send_message(SUPPORT_CHAT, "I'm alive!")
     
  
if __name__=="__main__":
    alive() 

