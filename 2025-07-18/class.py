import time
import requests
import random
import json

start_num = 1
end_num = 5
game_status = {} # храним данные об играх каждого пользователя
check_status = {}
del_status = {}
cour_status = {}
user_admin = 496775340
# keyboard = {"keyboard":[[{"text": "добавить дело"}], ]}
inline_keyboard = {
    'inline_keyboard':
    [
        [{'text': 'Сыграем', 'callback_data': 'play_game'}],
        [{'text': 'Управление покупками', 'callback_data': 'buy'}],
        [{'text': 'Прислать факт', 'callback_data': 'show_facts'}],
        [{'text': 'Конвертер валюты', 'callback_data': 'converter_course'}]
    ]
}



TOKEN = "dsadsads"

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

def send_buttons(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': 'Сыграем'}],
                [{'text': 'Управление покупками'}],
                [{'text': 'Прислать факт'}],
                [{'text': 'Конвертер валюты'}]
            ],
            'resize_keyboard': True,
            'one_time_keyboard': True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

def send_buttons_keyboard(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': inline_keyboard
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

def tovar_buttons(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': 'Добавить товар'}],
                [{'text': 'Удалить товар(ы)'}],
                [{'text': 'Список товаров'}],
                [{'text': 'Назад в главное меню'}]
            ],
            'resize_keyboard': True,
            'one_time_keyboard': True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

def send_facts(user_id):
    # генерируем факт
    with open('2025-07-18\\facts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    random_fact = random.choice(data)

    # Вывод результата
    cat = 'Категория: ' + random_fact['name']
    fact = 'Факт: ' + random_fact['fact']
    send_message(user_id, cat)
    send_message(user_id, fact)
    return

def start_game(user_id):
    # запускаем игру
    game_status[user_id] = {'right_answer': random.randint(start_num, end_num), 'attempts': 3, 'in_game': True}
    message = 'Угадай число от ' + str(start_num) + ' до ' + str(end_num) + '. У тебя 3 попытки'
    send_message(user_id, message)
    
def start_course(user_id):
    # запускаем конвертер
    cour_status[user_id] = {'course': True}
    message = 'Введи сумму в рублях для конвертации в доллары'
    send_message(user_id, message)
    
def start_add_tovar(user_id):
    check_status[user_id] = {'in_shop': True}
    message = 'Добавь товар и его стоимость через тире (-)'
    send_message(user_id, message)

def start_delete_tovar(user_id):
    del_status[user_id] = {'delete': True}
    message = 'Напиши название товара для удаления (или "все")'
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

def process_add_tovar(user_id, answer):
    # чекаем статус
    check_data = check_status[user_id]
    # чекаем введенные пользователем символы
    if answer.count('-') != 1:
        send_message(user_id, 'Некорректные входные данные (пример: "Название товара - 500")')
        check_data['in_shop'] = False
        return
    
    answer = answer.split('-')
    name = answer[0].strip()
    price = answer[1].strip()

    if name.lower() == 'все':
        send_message(user_id, 'Указано зарезервированное название товара)')
        check_data['in_shop'] = False
        return

    if len(answer) == 0:
        send_message(user_id, 'Неверно указано название товара (пример: "Название товара - 500")')
        check_data['in_shop'] = False
        return
    if len(price) == 0 and not price.isdigit() and int(price) == 0:
        send_message(user_id, 'Неверно указана цена товара (пример: "Название товара - 500")')
        check_data['in_shop'] = False
        return
    
    with open('2025-07-18\\buy.json', encoding='utf-8') as f:
        tovars = json.load(f)
    for w in tovars:
        if name == w['name']:
            send_message(user_id, 'Такой товар уже есть в списке покупок')
            check_data['in_shop'] = False
            return
    else:
        tovar = {
            "name": name,
            "price": price,
            "user_id": user_id
        }
        tovars.append(tovar)
        with open('2025-07-18\\buy.json', 'w', encoding='utf-8') as f:
            json.dump(tovars, f, ensure_ascii=True, indent=4)
        send_message(user_id, 'Товар добавлен')
        check_data['in_shop'] = False
        return

def process_delete_tovar(user_id, answer):
    # чекаем статус
    check_del = del_status[user_id]
    # чекаем введенные пользователем символы
    flag_tovar = False

    if answer.lower() == 'все':
        with open('2025-07-18\\buy.json', 'r', encoding='utf-8') as f:
            tovars = json.load(f)
        new_tovars = []
        for w in tovars:
            if w['user_id'] == user_id:
                continue
            else:
                new_tovars.append(w)
        with open('2025-07-18\\buy.json', 'w', encoding='utf-8') as f:
            json.dump(new_tovars, f, ensure_ascii=True, indent=4)
        send_message(user_id, 'Товары удалены')
        check_del['delete'] = False
        return

    if len(answer) == 0:
        send_message(user_id, 'Неверно указано название товара')
        check_del['delete'] = False
        return
    
    with open('2025-07-18\\buy.json', 'r', encoding='utf-8') as f:
        tovars = json.load(f)
    new_tovars = []
    for w in tovars:
        if w['name'] == answer and w['user_id'] == user_id:
            flag_tovar = True
            continue
        else:
            new_tovars.append(w)
    with open('2025-07-18\\buy.json', 'w', encoding='utf-8') as f:
        json.dump(new_tovars, f, ensure_ascii=True, indent=4)
    if flag_tovar:
        send_message(user_id, 'Товар удален')
    else:
        send_buttons(user_id, 'Нет такого товара')
    check_del['delete'] = False
    return

def process_list_tover(user_id):
    with open('2025-07-18\\buy.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        send_message(user_id, 'Вот Ваш список товаров:')
        for d in data:
            if d['user_id'] == user_id:
                mess = d['name'] + ' ' + str(d['price'])
                send_message(user_id, mess)
    return

def process_course(user_id, answer):
    # чекаем введенные пользователем символы
    if not answer.isdigit():
        send_message(user_id, 'Вы ввели не только цифры')
        return
    
    answers = int(answer)
    if answers == 0:
        message = 'Сумма для конвертации должна быть > 0'
        send_message(user_id, message)
        return
    
    cour_data = cour_status[user_id]

    urld = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(urld)
    usd_rate = response.json()['Valute']['USD']['Value']
    message = 'Вы получите: ' + str(int(answer) / usd_rate) + ' $'
    send_message(user_id, message)
    cour_data['course'] = False

def check_updates():
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)
        if updates.get('result'):
            for item in updates['result']:
                last_update_id = item['update_id'] + 1
                if 'callback_query' in item:
                    # send_message(user_id, 'hello')
                    callback_query = item['callback_query']
                    user_id = callback_query['from']['id']
                    callback_data = callback_query.get('data','')
                    print(callback_data)
                    if callback_data == 'show_facts':
                        send_facts(user_id)
                if 'message' in item:
                    message = item['message']
                    user_id = message['from']['id']
                    text = message.get('text', '')
                    
                    if text == 'Сыграем':
                        start_game(user_id)
                    elif text == 'Управление покупками':
                        tovar_buttons(user_id, 'Выбери действие из меню')
                    elif text == 'Назад в главное меню':
                        send_buttons(user_id, 'Выбери действие из меню')
                    elif text == 'Добавить товар':
                        start_add_tovar(user_id)
                    elif text == 'Конвертер валюты':
                        start_course(user_id)
                    elif user_id in check_status and check_status[user_id]['in_shop']:
                        process_add_tovar(user_id, text)
                    elif text == 'Удалить товар(ы)':
                        start_delete_tovar(user_id)
                    elif user_id in del_status and del_status[user_id]['delete']:
                        process_delete_tovar(user_id, text)
                    elif text == 'Список товаров':
                        process_list_tover(user_id)
                    elif user_id in game_status and game_status[user_id]['in_game']:
                        process_answer(user_id, text)
                    elif 'Прислать факт' in text:
                        send_facts(user_id)
                    elif user_id in cour_status and cour_status[user_id]['course']:
                        process_course(user_id, text)

        time.sleep(1)

send_buttons_keyboard(user_admin, 'Бот запущен. Выбери действие из меню')
check_updates()
