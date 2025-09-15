import time
import requests
import random

start_num = 1
end_num = 5
game_status = {} #храним данные об играх каждого пользователя
user_admin = 496775340

TOKEN = "dsadsa"

id_last_message = ''

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
    response = requests.get(url)
    return response.json()


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()

def start_game(user_id):
    # запускаем игру
    game_status[user_id] = {'right_answer': random.randint(start_num, end_num), 'attempts': 3, 'in_game': True}
    message = 'Угадай число от ' + str(start_num) + ' до ' + str(end_num) + '. У тебя 3 попытки'
    send_message(user_id, message)
    
def process_answer(user_id, answer):
    #чекаем введенные пользователем символы
    if not answer.isdigit():
        send_message(user_id, 'Вы ввели не только цифры')
        return
    
    answers = int(answer)
    if  not start_num <= answers <= end_num:
        message = 'Число должно быть от ' + str(start_num) + ' до ' + str(end_num) + '.'
        send_message(user_id, message)
    
    game_data = game_status[user_id]

    if answers == game_data['right_answer']:
        send_message(user_id, 'Молодец! Угадал!')
        game_data['in_game'] = False
        return
    
    game_data['attempts'] -= 1

    if game_data['attempts'] > 0:
        message = 'Не угадал:(. Осталось попыток: ' + str(game_data['attempts']) + '. правильный ответ - ' + str(game_data['right_answer'])
        send_message(user_id, message)
    else:
        message = 'Игра окончена. Я загадал число - ' + str(game_data['right_answer'])
        send_message(user_id, message)
        game_data['in_game'] = False

def check_updates():
    updates = get_updates()
    if updates['result']:
        id_last_message = updates['result'][0]['update_id']
    while True:
        updates = get_updates()
        if updates['result']:
            for item in updates['result']:
                if int(item['update_id']) > id_last_message:
                    user_id = item['message']['from']['id']
                    text = item['message']['text']
                    # print(f"Сообщение от пользователя: {user_id}, текст: {text}")
                    if text.lower() == 'сыграем':
                        start_game(user_id)
                    elif user_id in game_status and game_status[user_id]['in_game']:
                        process_answer(user_id, text)
                    id_last_message = int(item['update_id'])
        time.sleep(1)
send_message(user_admin, 'бот запущен')
check_updates()

