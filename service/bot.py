from dotenv import load_dotenv
import os
import telebot as tb
from telebot import types
from config.database import SessionLocal
from service.utils import verify_password
from models.users import User


load_dotenv()


api = os.environ.get('BOT_API')
bot = tb.TeleBot(api)


@bot.message_handler(commands=['start'])
def first_launch(message: types.Message) -> None:
    send = bot.send_message(message.chat.id, 'Первый запуск. Напиши логин и пароль:')
    bot.register_next_step_handler(send, auth)


def auth(message: types.Message) -> None:
    data = message.text.split()
    db = SessionLocal()
    try:
        db_user = db.query(User).filter(User.email == data[0]).first()
    finally:
        db.close()

    if db_user is None:
        bot.send_message(message.chat.id, 'Неверный логин или пароль')
    hash_password = db_user.password
    if not verify_password(data[1], hash_password):
        bot.send_message(message.chat.id, 'Неверный логин или пароль')
    bot.send_message(message.chat.id, 'конфетка')



if __name__ == '__main__':
    bot.infinity_polling()
