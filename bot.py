from telegram import *
from telegram.ext import *
from ast import literal_eval

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

    # try:
    text = update.message.text

    if "+" in text:
        arr = text.split("+")
        cal = "+"
    if "-" in text:
        arr = text.split("-")
        cal = "-"
    if "*" in text:
        arr = text.split("*")
        cal = "*"
    if "/" in text:
        arr = text.split("/")
        cal = "/"

    first_num = literal_eval(arr[0].replace(",","").strip())
    last_num = literal_eval(arr[1].replace(",","").strip())
    result = eval(text.replace(",",""))

    msg = f'{first_num:,} {cal} {last_num:,} = {result:,}'

    await context.bot.send_message(chat_id, text=msg, parse_mode=constants.ParseMode.HTML)
    # except:
    #     print("An exception occurred")

app = ApplicationBuilder().token(
    "5974270430:AAHbYv4dSgycHWrL4Q5q8k_P2vigIa89kig").build()

# app = ApplicationBuilder().token(
#     "6217705988:AAEOYp5g31rkl-iWrXAGE_mo7t0f0Oz3qIo").build()

app.add_handler(CommandHandler("start", start)) 
app.add_handler(MessageHandler(filters.ALL, messageHandler))

app.run_polling()