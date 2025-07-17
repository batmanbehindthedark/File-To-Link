from Achyuth.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Achyuth import StartTime


START_TEXT = """ Your Telegram DC Is : `{}`  """


@StreamBot.on_message(filters.regex("Maintained By @TmaAddaa"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="I was developed By [BRUCE WAYNE](https://t.me/BrUcE_ReTiReD_PiRaTe)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Developer💻", url=f"https://t.me/BrUcE_ReTiReD_PiRaTe"),
                                InlineKeyboardButton('⌬ Movies Bot', url=f"https://t.me/TGM_FILES_BOT")
                            ],[
                                InlineKeyboardButton('🍀 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟs 🍀',  url="https://t.me/TG_Movies4u")
                            ]
                                
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("follow❤️"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>HERE'S THE FOLLOW LINK</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("FOLLOW ME", url=f"https://t.me/TG_Movies4u")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.command("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

    
    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3. `login🔑` \n 4.`follow❤️` \n 5. `ping📡` \n 6. `status📊` \n 7. `DC` this tells your telegram dc \n 8. `maintainers😎` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@StreamBot.on_message(filters.command("ping"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"Pong!\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.command("status"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = (
    f"<b>Bot Uptime:</b> {currentTime}\n"
    f"<b>Total disk percentage:</b> {disk} \n"
    f"<b>Used:</b> {recv} \n"
    f"📊Data Usage📊\n<b>Total Upload:</b> {sent}\n"
    f"<b>Total Download:</b> {recv}\n\n"
    f"<b>CPU:</b> {cpuUsage}% "
    f"<b>RAM:</b> {memory}% "
    f"<b>Disk:</b> unlimited %"
  )

  await update.reply_text(botstats)
