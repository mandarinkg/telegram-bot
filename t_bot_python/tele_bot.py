# import telebot, webbrowser
#
# bot = telebot.TeleBot('8549188571:AAFLVGUlG0X4C0OYFZMkWVV8bgQPnJkW9JE')
#
#
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, webbrowser.open('https://telegram.me/tel_bot'))
#
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'чтобы знать придется вам ждать ответ')
#
#
# @bot.message_handler()
# def edit_message(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message.chat.id, f'your id is {message.from_user.id}')
#
#
# bot.polling(none_stop=True)