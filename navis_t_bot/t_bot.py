import telebot
import pyjokes
import random
from telebot import types

bot = telebot.TeleBot('8373326474:AAHH4-g-MTd0zSXhex4pbR5d3mU0Ym9H3Ws')

# условия
# @bot.message_handler()
# def info_user(message):
#     if message.text.lower() == 'course':
#         bot.reply_to(message, 'я учусь курс программирование в navis')
#     elif message.text.lower() == 'info':
#         bot.reply_to(message, f'my name is {message.from_user.first_name}, I am 21 years old')
#     elif message.text.lower() == 'hello':
#         bot.reply_to(message, f'Hello my friend {message.from_user.first_name}')
#     else:
#         bot.reply_to(message, f'у меня нет такая команда   {message.text.upper()}')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Как твое дело {message.from_user.first_name} у мкеня есть эти комманды  course, info, hello')


@bot.message_handler(commands=['joke'])
def joke(message):
    j = pyjokes.get_joke(language='ru')
    bot.reply_to(message, j)




text = ['beatiful', 'good img', 'ohooo', 'molodec','bop ketkensingo']

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, random.choice(text))


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти на github', url='https://github.com/mandarinkg'))
    markup.add(types.InlineKeyboardButton('открыть chatgpt', url='https://chatgpt.com'))

    bot.reply_to(message, 'эти ссылки на сайты', reply_markup=markup)


bot.polling()