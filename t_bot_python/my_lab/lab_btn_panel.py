import telebot
import sqlite3
from telebot import types
from telebot.apihelper import close

bot = telebot.TeleBot('8549188571:AAFLVGUlG0X4C0OYFZMkWVV8bgQPnJkW9JE')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('список пользователей')
    btn2 = types.KeyboardButton('Добавить пользователя')
    btn3 = types.KeyboardButton('удалить пользователя')
    markup.add(btn1, btn2, btn3)

    bot.reply_to(message, f'Привет, {message.from_user.first_name} выберите один из кнопку в панеле, /start работает один раз после нажатие кнопки заново нажмите /start', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'список пользователей')
def name_users(message):
    conn = sqlite3.connect('usersLab.sql')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
    """)
    users = cursor.fetchall()

    conn.close()

    if not users:
        bot.send_message(message.chat.id, 'Пользователей нет')
        return

    text = "📋 Список пользователей:\n\n"
    for user_id in users:
        text += f'ID: {user_id[0]}\nname: {user_id[1]}\npsw: {user_id[2]}\n\n'

    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == 'Добавить пользователя')
def add_users(message):
    bot.send_message(message.chat.id, 'Введите имя пользователя:')
    bot.register_next_step_handler(message, save_user)

def save_user(message):
    global name
    name = message.text.strip()

    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, save_psw)

def save_psw(message):
    password = message.text.strip()
    conn = sqlite3.connect('usersLab.sql')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, psw) VALUES (?, ?)
    """, (name, password))
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, f"Пользователь {name} добавлен!")


@bot.message_handler(func=lambda message: (message.text or "").lower() == 'удалить пользователя')
def delete_user(message):
    bot.reply_to(message, 'выберите id пользователя')
    bot.register_next_step_handler(message, del_user)

def del_user(message):
    parts = message.text.split()

    # if isinstance(parts, int):
    #     return

    if len(parts) < 1:
        bot.send_message(message.chat.id, 'выберите id')
        return

    user_id = parts[0]

    conn = sqlite3.connect('usersLab.sql')
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users WHERE id = ?
    """, (user_id,))
    conn.commit()

    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, f'пользователь {user_id} удалено')


# @bot.message_handler(func=lambda message:True)
# def debug(message):
#     print('debug', message)
#     print('text', message.text)





bot.polling(non_stop=True)