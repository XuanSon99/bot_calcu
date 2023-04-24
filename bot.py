from telegram import *
from telegram.ext import *

qr = "👨‍💻 Tạo mã QR"

domain = "https://chootc.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = [[KeyboardButton(qr)]]

    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    text = "- Ký hiệu: Cộng (+), Trừ (-), Nhân (*), Chia (/).\n- Bạn có thể dùng dấu phẩy (,) để ngăn cách chữ số hàng nghìn."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=constants.ParseMode.HTML)


async def messageHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    if update.message.chat.type != "private":
        return
    
    text = update.message.text

    msg = f'{text} = {eval(text.replace(",","")):,}'  

    await context.bot.send_message(chat_id, text=msg, parse_mode=constants.ParseMode.HTML)


app = ApplicationBuilder().token(
    "6269543727:AAFpuVDGiM4MMQXqg6ztcSRa2zd5GCOz6rg").build()

app.add_handler(CommandHandler("start", start)) 
app.add_handler(MessageHandler(filters.ALL, messageHandler))

app.run_polling()