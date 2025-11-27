import telebot
from telebot import types

bot = telebot.TeleBot('8549188571:AAFLVGUlG0X4C0OYFZMkWVV8bgQPnJkW9JE')

@bot.message_handler(commands=['menu'])
def send_menu(message):
    m = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('button1')
    btn2 = types.KeyboardButton('button2')
    m.add(btn1, btn2)

    bot.send_message(message.chat.id, 'choose button', reply_markup=m)

@bot.message_handler(func=lambda message: message.text in ['button1', 'button2'])
def send_message(message):
    if message.text == 'button1':
        bot.send_message(message.chat.id, 'you najal button 1')
    elif message.text == 'button2':
        bot.send_message(message.chat.id, 'you najal button 2')



bot.polling()