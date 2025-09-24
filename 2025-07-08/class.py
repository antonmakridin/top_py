import requests
from pprint import pprint
TOKEN = 'dsadsa' 

def check_bot():
    url = f'https://api.telegram.org/bot{TOKEN}/getMe'  
    response = requests.get(url)
    print(response.json())

def check_message():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    pprint(response.json())

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()

check_message()
# user_id = '496775340'
# print(send_message(user_id,'Привет'))