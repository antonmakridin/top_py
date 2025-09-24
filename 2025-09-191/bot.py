import telebot
from telebot import types
import yandextranslate
from speech import synthesize
from recognition import recognize

yandex = yandextranslate.YandexGPT()

from db import TelegramDB

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
db = TelegramDB('2025-09-191\\tg.json')

class Keyboards:
    def get_language_menu(self):
        markup_inline = types.InlineKeyboardMarkup()
        markup_inline.add(types.InlineKeyboardButton('английский', callback_data='lang=en'))
        markup_inline.add(types.InlineKeyboardButton('французский', callback_data='lang=fr'))
        markup_inline.add(types.InlineKeyboardButton('португальский', callback_data='lang=португальский'))
        return markup_inline

keyboard = Keyboards()

@bot.message_handler(commands=['start'])
def send_hello(message):
    # создать кнопки в интерфейсе
    markup_inline = keyboard.get_language_menu()

    bot.send_message(message.chat.id, 'Привет! Выбириай язык для перевода', reply_markup=markup_inline)

@bot.message_handler(commands=['language'])
def change_language(message):
    markup_inline = keyboard.get_language_menu()
    bot.send_message(message.chat.id, 'Выбириай язык для перевода', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: 'lang' in call.data)
def set_language(update):
    from pprint import pprint
    chat_id = update.message.chat.id
    lang = update.data.split('=')[1]
    db.set_value(chat_id, 'lang', lang)
    bot.send_message(chat_id, 'Пиши сообщения для первода')

@bot.callback_query_handler(func=lambda call: call.data == 'start_dialog')
def start_dialog(update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id, f'Начали диалог. Пиши сообщения - буду переводить')

@bot.message_handler(func=lambda message: True)
def get_text(message):
    lang = db.get_value(message.chat.id, 'lang')
    if lang:
        bot.send_message(message.chat.id, 'вот перевод')
        translation = yandex.get_answer(f'Переведи на {lang} текст: {message.text}')
        bot.send_message(message.chat.id, translation)

        voice = synthesize(translation)
        bot.send_voice(message.chat.id, voice)

    else:
        bot.send_message(message.chat.id, 'Не выбран язык для перевода')
        # Предлагаем выбрать язык
        markup_inline = keyboard.get_language_menu()
        bot.send_message(message.chat.id, 'Выберите язык:', reply_markup=markup_inline)

@bot.message_handler(content_types=['voice'])
def get_voice(message):
    voice = message.voice
    file_info = bot.get_file(voice.file_id)
    text = recognize(file_info.file_path)
    print(text)

bot.infinity_polling()