import telebot
import yandexkey
from telebot import types


API_TOKEN = '73055516dsapd2M4mSc'
bot = telebot.TeleBot(API_TOKEN)
yandex = yandexkey.YandexGPT()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Клавиатура
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Кнопки
    btn_ekb = types.InlineKeyboardButton('Екатеринбург', callback_data='city_ekb')
    btn_moscow = types.InlineKeyboardButton('Москва', callback_data='city_moscow')
    btn_spb = types.InlineKeyboardButton('Санкт-Петербург', callback_data='city_spb')
    
    # Добавляем кнопки в клавиатуру
    markup.add(btn_ekb, btn_moscow, btn_spb)
    
    # Отправляем сообщение с клавиатурой
    bot.send_message(
        message.chat.id,
        "Привет! Выбери город, чтобы узнать о нем больше:",
        reply_markup=markup
    )

# Один хэндлер для всех callback-запросов, начинающихся с 'city_'
@bot.callback_query_handler(func=lambda call: call.data.startswith('city_'))
def handle_city_click(call):
    city_names = {
        'ekb': 'Екатеринбург',
        'moscow': 'Москва', 
        'spb': 'Санкт-Петербург'
    }
    
    city_key = call.data.split('_')[1]
    city_name = city_names.get(city_key, 'Город')
    
    # Использование YandexGPT вместо предопределенных описаний
    description = yandex.get_answer(f'Напиши краткое описание города {city_name} на русском языке (2-3 предложения)')
    
    bot.send_message(call.message.chat.id, description)
    bot.answer_callback_query(call.id)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()