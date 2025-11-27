import telebot
from telebot import types

bot = telebot.TeleBot('8549188571:AAFLVGUlG0X4C0OYFZMkWVV8bgQPnJkW9JE')

"""  работа с кнопками  
add,
row, 
markup = types.InlineKeyboardMarkup()
types.InlineKeyboardButton('перейти git Намазбека', url='https://github.com/mandarinkg'),


"""
# @bot.message_handler(commands=['start'])
# def btn_start(message):
#     markup = types.InlineKeyboardMarkup()
#     # 1 способ
#     # markup.add(types.InlineKeyboardButton('перейти git Намазбека', url='https://github.com/mandarinkg'))
#     # markup.add(types.InlineKeyboardButton('отправить код', callback_data='getKod'))
#
#     # 2 способ
#     btn1 = types.InlineKeyboardButton('перейти git Намазбека', url='https://github.com/mandarinkg')
#     btn2 = types.InlineKeyboardButton('отправить код', callback_data='getKod')
#     btn3 = types.InlineKeyboardButton('перейти в анг группу', url='https://t.me/+YgN0jUoURQdiYjcy')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#
#     bot.reply_to(message, ' hello', reply_markup=markup)



"""  действие с кнопками, callback_data, удалить и изменить текст  
content_types=['photo', 'audio'],
callback_data='delete',
callback_data='edit',
@bot.callback_query_handler(func=lambda call: True),
call.data == 'delete',
call.data == 'edit',


"""
# @bot.message_handler(content_types=['photo'])
# def photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('перейти git Намазбека', url='https://github.com/mandarinkg')
#     btn2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#
#     bot.reply_to(message, 'beatifful photo' , reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == 'delete':
#         bot.delete_message(call.message.chat.id, call.message.message_id-1)
#     elif call.data == 'edit':
#         bot.edit_message_text('вы изменили текст', call.message.chat.id, call.message.message_id)


"""  создадим кнопку на панеле клавиатуру => 
types.ReplyKeyboardMarkup(), 
types.KeyboardButton(слова в кнопке),
bot.register_next_step_handler(message, function),

"""
# @bot.message_handler(commands=['start'])
# def btn_panel(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('перейти git Намазбека')
#     btn2 = types.KeyboardButton('удалить фото')
#     btn3 = types.KeyboardButton('изменить текст')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'каждая кнопка работает один раз, чтобы използовать еще нажмите /start заново ', reply_markup=markup)
#
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'перейти git Намазбека':
#         bot.reply_to(message, 'website is open')
#     elif message.text == 'удалить фото':
#         bot.reply_to(message, 'delete')



"""  отправка пользователю фото, аудио 

file = open('./img_aud/t_bot_im.jpeg', 'rb')
bot.send_photo(message.chat.id, file) => for photo

file = open('./img_aud/t_bot_im.mp3', 'rb')
bot.send_audio(message.chat.id, file) => _mp3_ for audio

file = open('./img_aud/t_bot_im.mp4', 'rb')
bot.send_video(message.chat.id, file) => _mp4_ for video
"""
@bot.message_handler(commands=['start'])
def btn_panel(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('перейти git Намазбека 😎')
    btn2 = types.KeyboardButton('удалить фото 🌅')
    btn3 = types.KeyboardButton('изменить текст')
    markup.row(btn1)
    markup.row(btn2, btn3)

    file = open('./img_aud/t_bot_im.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'каждая кнопка работает один раз, чтобы използовать еще нажмите /start заново ', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'перейти git Намазбека 😎':
        bot.reply_to(message, 'website is open')
    elif message.text == 'удалить фото 🌅':
        bot.reply_to(message, 'delete')

bot.polling(none_stop=True)