import requests

class TelegramAPI:
    
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_me(self):
        url = self.base_url + 'getMe'
        response = requests.get(url)
        # print(url)
        return response.json()
    
    def get_updates(self):
        """Получение обновлений"""
        url = self.base_url + 'getUpdates'
        response = requests.get(url)
        return response.json()
    
    def send_message(self, chat_id, message_text):
        """Отправка сообщений"""
        url = self.base_url + 'sendMessage'
        params = {'chat_id': chat_id, 'text': message_text}
        response = requests.post(url, json=params)
        return response.json()
    
token = "7305551623:AAHXWHs6FhqlctegHnVUYhhq_MQFyab9ddw"
MY_CHAT = 496775340
bot = TelegramAPI(token)

print(bot.get_updates())
print(bot.send_message(MY_CHAT,'привет'))


