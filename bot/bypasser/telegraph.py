from bot import telegraph, logger, app
from pyrogram import filters
import os


def convertTelegraph(data):
    post_content = "".join(f"<img src={link}><br>" for link in data)
    post = telegraph.create_page(
        nam,
        html_content=post_content,
    )
    return post


@app.on_message(filters.command("tgt"))
async def graphoo(_, msg):
    """function"""
    
    user = msg.from_user
    
    try:
        title = user.first_name
    except:
        title = "@URLBypasserBot"
            
        
    if msg.reply_to_message:
        content = msg.reply_to_message
        x = await msg.reply_text(f"Pasting {content.link} to telegraph!")
        
            
        if content.document and (content.document.file_size<(10 * 1024**2)):
            
            try:
                path = await content.download()
                m_list = None
                page_content = ""
                with open(path, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(path)
                text = page_content.replace("\n", "<br>")
                
            except Exception as e:
                logger.error(e, "caused by FUNC: graphoo")
                await msg.reply_text(f"Sorry some error excured\nERROR: {e}")
                await x.delete()
                return
        
        else:
            try:
                text = content.text.html.replace("\n", "<br>")
            except:
                await msg.reply_text("Please Reply to a Text or Document")
                await x.delete()
                return
    
    else:
        x = await msg.reply_text(f"Pasting {msg.link} to telegraph!")
        
        m = msg.text.split()
        if len(m)<2:
            await msg.reply_text("Format: /tgt <reply_to_msg/text>", parse_mode="markdown")
            await x.delete()
            return
        text = m[1]
    
    response = telegraph.create_page(
                title,
                html_content=text
            )
    
    await msg.reply_text("Pasted to [Telegraph](https://graph.org/{})".format(response["path"]))

    await x.delete()
