import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('8549188571:AAFLVGUlG0X4C0OYFZMkWVV8bgQPnJkW9JE')
name = None


"""
conn.commit() => синхронизация информации
cursor.close() => закроем курсор
conn.close() => закроем conn
"""
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('itproger.sql')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            psw TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас вас будем зарегистрировать, пишите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль ')
    bot.register_next_step_handler(message, user_psw)

def user_psw(message):
    password = message.text.strip()

    conn = sqlite3.connect('itproger.sql')
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO users 
            (name, psw) VALUES (?, ?)
        """,(name, password))
    conn.commit()
    cursor.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список всех пользователей', callback_data='users_list'))

    bot.send_message(message.chat.id, 'вы зарегистрированы', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    info = ''
    for el in users:
        info += f'пользователь: {el[0]} \nName: {el[1]} \nPassword: {el[2]}\n\n '

    cursor.close()
    conn.close()

    # markup = telebot.types.InlineKeyboardMarkup()
    bot.send_message(call.message.chat.id, info)
    # markup.add(telebot.types.InlineKeyboardButton('удалить пользователя', callback_data='delete_user'))

@bot.message_handler(commands=['del'])
def delete_user(message):
    parts = message.text.split()

    if len(parts) < 2:
        bot.send_message(message.chat.id, 'Използовать ID')
        return

    user_id = parts[1]

    conn = sqlite3.connect('itproger.sql')
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM users WHERE id = ?""", (user_id,))
    conn.commit()

    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, f'user deleted {user_id}')



bot.polling(none_stop=True)