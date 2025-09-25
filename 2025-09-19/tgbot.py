import telebot
from telebot import types
import yandexkey

yandex = yandexkey.YandexGPT()
bot = telebot.TeleBot("")

def en(text):
     return yandex.get_answer(f'Переведи на английский следующий текст: {text}')

def fr(text):
     return yandex.get_answer(f'Переведи на французский следующий текст: {text}')

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton('Английский', callback_data='lang=en'))
    markup_inline.add(types.InlineKeyboardButton('Французский', callback_data='lang=fr'))
    bot.send_message(message.chat.id, "Привет, выбирай язык для перевода:", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: call.data == 'joke')
def handle_callback(call):
	bot.answer_callback_query(call.id, "Кнопка нажата!")
	bot.send_message(call.message.chat.id, yandex.get_answer('Расскажи историчческий факт'))





# @bot.message_handler(func=lambda message: message.text == "Привет")
# def text_handler(message):
#     bot.send_message(message.chat.id, "Привет-привет!")

# @bot.message_handler(func=lambda message: message.text == "help")
# def text_handler(message):
#     bot.send_message(message.chat.id, "давай помогу!")


@bot.message_handler(func=lambda message: True)
def text_handler(message):
    bot.send_message(message.chat.id, "команда не распознана")

@bot.callback_query_handler(func=lambda call: 'lang' in call.data)
def set_language(update):
    # bot.answer_callback_query(update.id, "Кнопка нажата!")
    bot.send_message(update.message.chat.id, f'выбран язык: {update.data}')
    lang = update.data.split('=')[1]

bot.infinity_polling()