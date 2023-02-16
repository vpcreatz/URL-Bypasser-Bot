#Maybe uh... later?

import glob
import urllib
import img2pdf
from bot import app
from pyrogram import filters
import os

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'), ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'), ('Accept-Encoding','gzip, deflate, br'),\
    ('Accept-Language','en-US,en;q=0.5' ), ("Connection", "keep-alive"), ("Upgrade-Insecure-Requests",'1')]
urllib.request.install_opener(opener)


def save(imgurl, filename):
    urllib.request.urlretrieve(imgurl, filename+".jpg")
    

@app.on_message(filters.command('imgtopdf'))
def convertPDF(_, message):
    msg = message.text.split(" ", 1)[1].rsplit(" ", 1)
    data= msg[1].replace("['", "").replace("']", "").replace(";", "").split("', '")
    name = msg[2]

    os.mkdir(name)
    for _ in data:
        flnm=f"{name}/{data.index(_)}"
        save(_, flnm)
        
    with open(f"{name}s.pdf","wb") as f:
        f.write(img2pdf.convert(glob.glob(f"{name}/*.jpg")))
    message.reply_document(f"{name}s.pdf")
