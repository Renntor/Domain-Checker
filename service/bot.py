from dotenv import load_dotenv
import os
import telebot as tb

load_dotenv()


def start_bot():
    api = os.environ.get('BOT_API')
    bot = tb.TeleBot(api)
