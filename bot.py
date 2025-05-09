from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        KeyboardButton(text=" فیلم ببینیم!️", web_app=WebAppInfo(url="https://dooorbin.com/"))
    ]
    await update.message.reply_text(
        "روی یکی از دکمه‌های زیر بزن:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run_polling()