import requests
import time
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
        params = {'offset': offset + 1}
        response = requests.get(url, params=params)
        return response.json()
    
    def send_message(self, chat_id, message_text):
        """Отправка сообщений"""
        url = self.base_url + 'sendMessage'
        params = {'chat_id': chat_id, 'text': message_text}
        response = requests.post(url, json=params)
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

# def send_hello(chat_id):
#     telegram_api.send_message(chat_id, 'Стартуем бот!')

# def send_help(chat_id):
#     telegram_api.send_message(chat_id, 'Давай помогу!')

# def send_fact(chat_id):
#     telegram_api.send_message(chat_id, yandex.get_answer('случайный факт'))
    
token = "7305551623:AAHXWHs6FhqlctegHnVUYhhq_MQFyab9ddw"
MY_CHAT = 496775340

telegram_api = TelegramAPI(token)
bot = Bot(telegram_api)
yandex = YandexGPT()
# подключение хэндлеров
handlers = {}


start_handler = MessageHandler('/start', send_hello)
help_handler = MessageHandler('/help', send_help)
fact_handler = MessageHandler('случайный факт', send_fact)
bot.handlers.append(start_handler)
bot.handlers.append(help_handler)
bot.handlers.append(fact_handler)

bot.run()