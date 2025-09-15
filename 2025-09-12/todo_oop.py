import requests
import time
import os
import random
from yandex import YandexGPT

class TelegramAPI:
    
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_me(self):
        url = self.base_url + 'getMe'
        response = requests.get(url)
        return response.json()
    
    def get_updates(self, offset=0):
        """Получение обновлений"""
        url = self.base_url + 'getUpdates'
        params = {
            'offset': offset + 1
        }
        response = requests.get(url, params=params)
        return response.json()
    
    def send_message(self, chat_id, message_text):
        """Отправка сообщений"""
        url = self.base_url + 'sendMessage'
        params = {
            'chat_id': chat_id, 
            'photo': message_text
        }
        response = requests.post(url, json=params)
        return response.json()
    
    def send_photo(self, chat_id, random_jpg_file, caption):
        """Отправка сообщений"""
        url = self.base_url + 'sendPhoto'
        with open(random_jpg_file, 'rb') as photo_file:
            files = {'photo': photo_file}
            params = {'chat_id': chat_id, 'caption': caption}
            response = requests.post(url, files=files, data=params)
        response.raise_for_status()  # Проверяем статус ответа
        return response.json()
        

class Bot():
    def __init__(self, api:TelegramAPI):
        self.api = api
        self.last_update_id = 0
        self.handlers = []
        
    def run(self):
        while True:
            updates = self.api.get_updates(offset=self.last_update_id)['result']
            for update in updates:
                message = update['message']
                chat_id = message['chat']['id']
                text = message['text']
                # перебираем хэндлеры
                for handler in self.handlers:
                    # вызываем execute, в котором проверяется условие срабатывания хэндлера
                    handler.execute(text, chat_id)
                self.last_update_id = update['update_id']
            time.sleep(0.5)

class MessageHandler():
    def __init__(self, text, func):
        self.text = text
        self.func = func

    def execute(self, message_text, chat_id):
        if self.text == message_text:
            self.func(chat_id)

# функции
def send_hello(chat_id):
    telegram_api.send_message(chat_id, 'Стартуем бот!')

def send_help(chat_id):
    telegram_api.send_message(chat_id, 'Давай помогу!')

def send_fact(chat_id):
    telegram_api.send_message(chat_id, yandex.get_answer('случайный факт'))

def send_photo(chat_id):
    # Путь к папке с картинками
    folder_path = '2025-09-12\\img'
    if os.path.isdir(folder_path):
        # Получаем список всех файлов в папке
        all_files = os.listdir(folder_path)
     # Фильтруем список, оставляя только файлы с расширением .jpg
        jpg_files = [f for f in all_files if f.endswith('.jpg')]
     # Выбираем случайный файл из списка jpg-файлов
        if jpg_files:
            random_jpg_file = random.choice(jpg_files)
            random_jpg_file = folder_path + '\\' + random_jpg_file
            caption = 'Вот тебе картинка'
    else:
        random_jpg_file = '2025-09-12\\nophoto.jpg'
        caption = 'Не нашел картинку'
    
    telegram_api.send_photo(chat_id, random_jpg_file, caption)
    
token = "sss"
MY_CHAT = 496775340

telegram_api = TelegramAPI(token)
bot = Bot(telegram_api)
yandex = YandexGPT()
# подключение хэндлеров

start_handler = MessageHandler('/start', send_hello)
help_handler = MessageHandler('/help', send_help)
fact_handler = MessageHandler('случайный факт', send_fact)
photo_rnd_handler = MessageHandler('картинка', send_photo)

# обработчики
bot.handlers.append(start_handler)
bot.handlers.append(help_handler)
bot.handlers.append(fact_handler)
bot.handlers.append(photo_rnd_handler)

bot.run()