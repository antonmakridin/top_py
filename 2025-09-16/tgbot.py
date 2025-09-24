import telebot
from telebot import types
import yandexkey

yandex = yandexkey.YandexGPT()
bot = telebot.TeleBot("dsadsa")


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add(types.KeyboardButton("Расскажи анекдот"))
    # markup.add(types.KeyboardButton("Предсказание на завтра"))
    # кнопки в интерфейсе
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton('Расскажи анекдот', callback_data='joke'))
    bot.send_message(message.chat.id, "привет:", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: call.data == 'joke')
def handle_callback(call):
	bot.answer_callback_query(call.id, "Кнопка нажата!")
	bot.send_message(call.message.chat.id, yandex.get_answer('Расскажи историчческий факт'))

@bot.message_handler(func=lambda message: message.text == "Привет")
def text_handler(message):
    bot.send_message(message.chat.id, "Привет-привет!")

@bot.message_handler(func=lambda message: message.text == "help")
def text_handler(message):
    bot.send_message(message.chat.id, "давай помогу!")

@bot.message_handler(func=lambda message: message.text == "Про Вовочку")
def text_handler(message):
    bot.send_message(message.chat.id, 'Придумываю анекдот')
    bot.send_message(message.chat.id, yandex.get_answer('Расскажи анекдот про Вовочку'))

@bot.message_handler(func=lambda message: message.text == "Про киборгов")
def text_handler(message):
    bot.send_message(message.chat.id, 'Придумываю анекдот')
    bot.send_message(message.chat.id, yandex.get_answer('Расскажи анекдот про киборгов'))

@bot.message_handler(func=lambda message: message.text == "Предсказание на завтра")
def text_handler(message):
    bot.send_message(message.chat.id, 'Придумываю предсказание')
    bot.send_message(message.chat.id, yandex.get_answer('Придумай предсказание на завтра'))

@bot.message_handler(func=lambda message: True)
def text_handler(message):
    bot.send_message(message.chat.id, "команда не распознана")

bot.infinity_polling()