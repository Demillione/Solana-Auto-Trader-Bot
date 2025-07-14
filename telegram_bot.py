from telegram import Bot
import os

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))

def send_telegram_alert(message):
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot.send_message(chat_id=chat_id, text=message)