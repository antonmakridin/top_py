import time
import requests
import random
import json

start_num = 1
end_num = 5
game_status = {} # храним данные об играх каждого пользователя
user_admin = 496775340
variant_answer = ["Норм", "Хорошо", "Отлично!"]

TOKEN = "sdsadsa"

id_last_message = ''

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {'timeout': 10}
    if offset:
        params['offset'] = offset
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()

def send_game_button(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': 'Сыграем'}]
            ],
            'resize_keyboard': True,
            'one_time_keyboard': True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

def start_game(user_id):
    # запускаем игру
    game_status[user_id] = {'right_answer': random.randint(start_num, end_num), 'attempts': 3, 'in_game': True}
    message = 'Угадай число от ' + str(start_num) + ' до ' + str(end_num) + '. У тебя 3 попытки'
    send_message(user_id, message)
    
def process_answer(user_id, answer):
    # чекаем введенные пользователем символы
    if not answer.isdigit():
        send_message(user_id, 'Вы ввели не только цифры')
        return
    
    answers = int(answer)
    if not start_num <= answers <= end_num:
        message = 'Число должно быть от ' + str(start_num) + ' до ' + str(end_num) + '.'
        send_message(user_id, message)
        return
    
    game_data = game_status[user_id]

    if answers == game_data['right_answer']:
        send_message(user_id, 'Молодец! Угадал!')
        game_data['in_game'] = False
        return
    
    game_data['attempts'] -= 1

    if game_data['attempts'] > 0:
        message = 'Не угадал:(. Осталось попыток: ' + str(game_data['attempts']) + '.'
        send_message(user_id, message)
    else:
        message = 'Игра окончена. Я загадал число - ' + str(game_data['right_answer'])
        send_message(user_id, message)
        game_data['in_game'] = False

def check_updates():
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)
        if updates.get('result'):
            for item in updates['result']:
                last_update_id = item['update_id'] + 1
                
                if 'message' in item:
                    message = item['message']
                    user_id = message['from']['id']
                    text = message.get('text', '')
                    
                    if text == 'Сыграем':
                        start_game(user_id)
                    elif text.lower() == '/start':
                        send_game_button(user_id, 'Нажми кнопку "Сыграем", чтобы начать игру!')
                    elif user_id in game_status and game_status[user_id]['in_game']:
                        process_answer(user_id, text)
                    elif 'как дела' in text:
                        send_message(user_id, random.choice(variant_answer))
                    elif 'загадай число' in text:
                        send_message(user_id, f"Вот твое число: {random.randint(1, 10)}")

        time.sleep(1)

send_game_button(user_admin, 'Бот запущен. Нажми "Сыграем", чтобы начать игру!')
check_updates()