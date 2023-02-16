import subprocess
from bot import app, DEV_USERS
from pyrogram import filters

@app.on_message(filters.user(DEV_USERS) & filters.command('sh'))
async def shell(_, message):
    cmd = message.text.split(" ", 1)[1]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
    )
    stdout, stderr = process.communicate()
    stderr = stderr.decode()
    stdout = stdout.decode()
    Kek = ""
    if stdout:
        Kek += f"*Stdout*\n`{stdout}`\n"
    if stderr:
        Kek += f"*Stderr*\n`{stderr}`\n"
    if len(Kek) > 3000:
        with open("kek.txt", "w") as file:
            file.write(Kek)
        return await messages.reply_document("kek.txt")
    else:
        await message.reply_text(Kek)
