import requests
import time

user_admin = 496775340
id_last_message = ''

TOKEN = "sadsadsa"

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
    response = requests.get(url)
    return response.json()


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()


def check_updates():
    updates = get_updates()
    if updates['result']:
        id_last_message = updates['result'][0]['update_id']
    while True:
        updates = get_updates()
        if updates['result']:
            for item in updates['result']:
                if int(item['update_id']) > id_last_message:
                    user_name = item['message']['from']['first_name'] + ' ' + item['message']['from']['last_name']
                    text = item['message']['text']
                    if text.lower() == 'привет':
                        message = 'Привет ' + user_name
                        # print(f'Привет {message}')
                        send_message(user_admin, message)
                        id_last_message = int(item['update_id'])
        time.sleep(1)
send_message(user_admin, 'бот запущен')
check_updates()

