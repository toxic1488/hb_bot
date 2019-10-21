import json
import telebot
import time
import random
import os

token = os.environ.get('token', None)

bot = telebot.TeleBot(token)
print(bot)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Мотивация', 'Комплимент', 'Кто я?', 'Жалоба')
keyboard2.row('плохо')
pleasure = [
    'Нет, иди занимайся делом, нигер',
    'Не та кнопка',
    'Ты ошибся'
]

poshalim = [
    'CAADBQADtwMAAukKyANVVNJ3JC5xJBYE',
    'CAADAgAD0wQAAjbsGwU5qLzOO6SmQBYE',
    'CAADAgADGwEAAphsyApNnpj_e80uuRYE',
    'CAADAgADSioAAktqAwABYJfJOAN1P1MWBA'
]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, мой ,белый хозяин!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветствую тебя, мой ,белый хозяин!')
    elif message.text.lower() == 'мотивация':
        bot.send_message(message.chat.id, 'Если будешь плохо работать,\n'
                                          'Всю жизнь будешь\nездить на КАЛИНЕ', reply_markup=keyboard1)
    elif message.text.lower() == 'комплимент':
        bot.send_message(message.chat.id, random.choice(pleasure), reply_markup=keyboard1)
    elif message.text.lower() == 'плохо':
        bot.send_sticker(message.chat.id, 'CAADAgADAhUAAt8BNwABeYpnE7DZQiwWBA', reply_markup=keyboard1)
    elif message.text.lower() == 'пошалим':
        bot.send_message(message.chat.id, 'Приготовься')
        bot.send_sticker(message.chat.id, random.choice(poshalim), reply_markup=keyboard1)
    elif message.text.lower() == 'кто я?':
        bot.send_sticker(message.chat.id, 'CAADAgADpAEAAjbsGwUhIQa5_3ORpBYE', reply_markup=keyboard1)
    elif message.text.lower() == 'жалоба':
        bot.send_message(message.chat.id, 'Как я работаю?', reply_markup=keyboard2)
    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNh4AAulVBRgUGtr-2VDSWhYE')
        bot.send_message(message.chat.id, 'Нажимай на кнопки, нигер', reply_markup=keyboard1)


@bot.message_handler(content_types=['sticker', 'photo'])
def sticker_id(sticker):
    print(sticker)


# Executing
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
