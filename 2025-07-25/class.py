import time
import requests
import random
import json
import sys

start_num = 1
end_num = 5
game_status = {} # храним данные об играх каждого пользователя
check_status = {}
del_status = {}
edit_status = {}
cour_status = {}
user_admin = 496775340
# keyboard = {"keyboard":[[{"text": "добавить дело"}], ]}
main_menu = {
    'inline_keyboard':
    [
        [{'text': 'Управление делами', 'callback_data': 'delo'}],
        [{'text': 'Прислать факт', 'callback_data': 'show_facts'}]
    ]
}

dela_menu = {
    'inline_keyboard':
    [
        [{'text': 'Добавить дело', 'callback_data': 'add_delo'}],
        [{'text': 'Удалить дело(а)', 'callback_data': 'delete_delo'}],
        [{'text': 'Изменить статус', 'callback_data': 'edit_status_delo'}],
        [{'text': 'Список дел', 'callback_data': 'list_delo'}],
        [{'text': 'Назад в главное меню', 'callback_data': 'main_menu'}]
    ]
}

TOKEN = "dsadsa"

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
                [{'text': 'Управление делами'}],
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

def send_buttons_keyboard(chat_id, text, keyboard):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': keyboard
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

def dela_buttons(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': [
                [{'text': 'Добавить дело'}],
                [{'text': 'Удалить дело(а)'}],
                [{'text': 'Список дел'}],
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
    with open('2025-07-25\\facts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    random_fact = random.choice(data)

    # Вывод результата
    cat = 'Категория: ' + random_fact['name']
    fact = 'Факт: ' + random_fact['fact']
    send_message(user_id, cat)
    send_message(user_id, fact)
    send_buttons_keyboard(user_id, 'Выбери действие из меню',main_menu)
    return

def start_game(user_id):
    # запускаем игру
    game_status[user_id] = {'right_answer': random.randint(start_num, end_num), 'attempts': 3, 'in_game': True}
    message = 'Угадай число от ' + str(start_num) + ' до ' + str(end_num) + '. У тебя 3 попытки'
    send_message(user_id, message)
    
def start_add_delo(user_id):
    check_status[user_id] = {'in_delo': True}
    message = 'Введи название дела'
    send_message(user_id, message)

def start_delete_delo(user_id):
    del_status[user_id] = {'delete': True}
    message = 'Напиши номер задачи для удаления (или напиши "все", чтобы удалить все свои задачи)'
    send_message(user_id, message)

def start_edit_delo(user_id):
    edit_status[user_id] = {'edit': True}
    message = 'Напиши номер задачи для изменения статуса'
    send_message(user_id, message)

def process_add_delo(user_id, answer):
    # чекаем статус
    check_data = check_status[user_id]
    # чекаем введенные пользователем символы
    # if answer.count('-') != 1:
    #     send_message(user_id, 'Некорректные входные данные (пример: "Название дела)')
    #     check_data['in_delo'] = False
    #     return
    
    status = '0'
    if answer.find('-') != -1:
        answer = answer.split('-')
        name = answer[0].strip()
        status = answer[1].strip()
    else:
        name = answer

    if name.lower() == 'все':
        # send_message(user_id, 'Указано зарезервированное название)')
        send_buttons_keyboard(user_id, 'Указано зарезервированное название. Выбери действие из меню',dela_menu)
        check_data['in_delo'] = False
        return

    if len(answer) == 0:
        # send_message(user_id, 'Неверно указано название дела (пример: "Название дела")')
        send_buttons_keyboard(user_id, 'Неверно указано название дела (пример: "Название дела"). Выбери действие из меню',dela_menu)
        check_data['in_delo'] = False
        return
    if not status.isdigit() and int(status) > 1:
        # send_message(user_id, 'Неверно указан статус дела (пример: "Название дела - 0/1 (где 0 - не выполнено, 1 - выполнено)")')
        send_buttons_keyboard(user_id, 'Неверно указан статус дела (пример: "Название дела - 0/1 (где 0 - не выполнено, 1 - выполнено)"). Выбери действие из меню',dela_menu)
        check_data['in_delo'] = False
        return
    
    with open('2025-07-25\\dela.json', encoding='utf-8') as f:
        delas = json.load(f)
    for w in delas:
        if name == w['name']:
            # send_message(user_id, 'Такое дело уже есть в списке дел')
            send_buttons_keyboard(user_id, 'Такое дело уже есть в списке дел. Выбери действие из меню',dela_menu)
            check_data['in_delo'] = False
            return
    else:
        dela = {
            "name": name,
            "status": status,
            "user_id": user_id
        }
        delas.append(dela)
        with open('2025-07-25\\dela.json', 'w', encoding='utf-8') as f:
            json.dump(delas, f, ensure_ascii=True, indent=4)
        send_buttons_keyboard(user_id, 'Дело добавлено. Выбери действие из меню',dela_menu)
        check_data['in_delo'] = False
        return

def process_delete_delo(user_id, answer):
    # чекаем статус
    check_del = del_status[user_id]
    # чекаем введенные пользователем символы
    flag_dela = False

    if answer.lower() == 'все':
        with open('2025-07-25\\dela.json', 'r', encoding='utf-8') as f:
            delas = json.load(f)
        new_delas = []
        for w in delas:
            if w['user_id'] == user_id:
                continue
            else:
                new_delas.append(w)
        with open('2025-07-25\\dela.json', 'w', encoding='utf-8') as f:
            json.dump(new_delas, f, ensure_ascii=True, indent=4)
        send_buttons_keyboard(user_id, 'Задачи удалены. Выбери действие из меню',dela_menu)
        
        check_del['delete'] = False
        return

    if len(answer) == 0:
        send_buttons_keyboard(user_id, 'Неверно указано название задачи. Выбери действие из меню',dela_menu)
        check_del['delete'] = False
        return
    with open('2025-07-25\\dela.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    user_task_indexes = [i for i, d in enumerate(data) if d['user_id'] == user_id]

    # Проверяем, существует ли дело с таким номером
    if len(user_task_indexes) >= int(answer):
        # Получаем индекс элемента в основном списке data, который соответствует делу №2 у пользователя
        index_to_delete = user_task_indexes[int(answer) - 1]
        
        # Удаляем этот элемент
        deleted_task = data.pop(index_to_delete)
        message = 'Удалено дело: ' + deleted_task['name']
        send_message(user_id, message)
        send_buttons_keyboard(user_id, 'Выбери действие из меню',dela_menu)
    else:
        send_message(user_id, 'Дело с таким номером не найдено')
        send_buttons_keyboard(user_id, 'Выбери действие из меню',dela_menu)
    with open('2025-07-25\\dela.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=True, indent=4)
    check_del['delete'] = False
    return

def process_list_dela(user_id):
    with open('2025-07-25\\dela.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        send_message(user_id, 'Вот Ваш список дел:')
        filtered_data = [d for d in data if d['user_id'] == user_id]
        message = []
        for index, d in enumerate(filtered_data, start=1):
            status = 'выполнено' if d['status'] == '1' else 'не выполнено'
            message.append(f"{index}. {d['name']} - {status}")
        full_message = "\n".join(message)
        send_message(user_id, full_message)
        send_buttons_keyboard(user_id, 'Выбери действие из меню',dela_menu)
    return

def process_edit_dela(user_id, answer):
    # Чтение данных из файла
    with open('2025-07-25\\dela.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Фильтрация дел по user_id
    filtered_data = [d for d in data if d['user_id'] == user_id]
    answer = int(answer)
    # Проверяем, что номер в допустимом диапазоне
    if 1 <= answer <= len(filtered_data):
        # Находим соответствующее дело в отфильтрованном списке
        selected_delo = filtered_data[answer - 1]

        # Находим это дело в исходных данных для изменения
        for d in data:
            if d['user_id'] == user_id and d['name'] == selected_delo['name']:
                # Меняем статус на противоположный
                d['status'] = '1' if d['status'] == '0' else '0'
                break
            
        # Записываем изменения обратно в файл
        with open('2025-07-25\\dela.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        send_message(user_id, f'Статус дела "{selected_delo["name"]}" изменен!')
    else:
        send_message(user_id, 'Некорректный номер дела.')
    
    # Вывод списка дел
    send_message(user_id, 'Вот Ваш список дел:')
    message = []
    for index, d in enumerate(filtered_data, start=1):
        status = 'выполнено' if d['status'] == '1' else 'не выполнено'
        message.append(f"{index}. {d['name']} - {status}")
    
    full_message = "\n".join(message)
    send_message(user_id, full_message)
    send_buttons_keyboard(user_id, 'Выбери действие из меню', dela_menu)
    return

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
                    if callback_data == 'show_facts':
                        send_facts(user_id)
                    elif callback_data == 'delo':
                        send_buttons_keyboard(user_id, 'Выбери действие из меню',dela_menu)
                    elif callback_data == 'main_menu':
                        send_buttons_keyboard(user_admin, 'Выбери действие из меню', main_menu)
                    elif callback_data == 'add_delo':
                        start_add_delo(user_id)
                    elif callback_data == 'list_delo':
                        process_list_dela(user_id)
                    elif callback_data == 'delete_delo':
                        start_delete_delo(user_id)
                    elif callback_data == 'edit_status_delo':
                        start_edit_delo(user_id)
                if 'message' in item:
                    message = item['message']
                    user_id = message['from']['id']
                    text = message.get('text', '')
                    
                    if '/start' in text:
                        send_buttons_keyboard(user_admin, 'Выбери действие из меню', main_menu)
                    elif user_id in check_status and check_status[user_id]['in_delo']:
                        process_add_delo(user_id, text)
                    elif user_id in del_status and del_status[user_id]['delete']:
                        process_delete_delo(user_id, text)
                    elif user_id in edit_status and edit_status[user_id]['edit']:
                        process_edit_dela(user_id, text)

        time.sleep(1)

send_buttons_keyboard(user_admin, 'Бот запущен. Выбери действие из меню', main_menu)
check_updates()
