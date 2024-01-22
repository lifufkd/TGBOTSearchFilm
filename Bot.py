import telebot
from telebot import types

bot = telebot.TeleBot('6723388582:AAFgzZfo9KG-UE8ZDKkxsyylwLJMAkEXms4')


@bot.message_handler(commands=['start', 'creators'])
def start(message):
    command = message.text.replace('/', '')
    if command == 'start':
        markup = types.InlineKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'Привет👋\nЯ SearchFilmBot🤖 - помогу с поиском интересного фильма!\nНапишите /creators для получения информации о создателях.')
        btn1 = types.InlineKeyboardButton('Жанры', callback_data='genre')
        btn2 = types.InlineKeyboardButton('Года', callback_data='years')
        btn3 = types.InlineKeyboardButton('Поиск по названию', callback_data='name')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите действие✅', reply_markup=markup)
    elif command == 'creators':
        markup = types.InlineKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'Создатели:\nzzsxd - фронтенд составляющая бота.\nSBR - бэкенд составляющая бота.')
        btn1 = types.InlineKeyboardButton('Жанры', callback_data='genre')
        btn2 = types.InlineKeyboardButton('Года', callback_data='years')
        btn3 = types.InlineKeyboardButton('Поиск по названию', callback_data='name')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите действие✅', reply_markup=markup)


@bot.message_handler(content_types=['photo', 'video', 'voice', 'audio', 'image', 'sticker', 'text'])
def text(message):
    if message.text is None:
        bot.reply_to(message, '🚫Ошибка: неверный формат ввода🚫')
    else:
        pass




@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'genre':
        print('Пользователь нажал кнопку: "Жанры"')
        bot.send_message(call.message.chat.id, '😭Введите жанр фильма🤣')
    elif call.data == 'years':
        print('Пользователь нажал кнопку: "Года"')
        bot.send_message(call.message.chat.id, '🕜Введите диапазон лет🕜')
    elif call.data == 'name':
        print('Пользователь нажал кнопку "Поиск по названию"')
        bot.send_message(call.message.chat.id, '📽Введите название фильма📽')

bot.polling(none_stop=True)