import time
import requests

TOKEN = "7305551623:AAH0quKy8Rc5zVkl2FkXlD3G75C0xurWvi0"
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def get_updates():
    response = requests.get(URL)
    return response.json()

# updates = get_updates()
# if updates['result']:
#     for item in updates['result']:
#         ts = item['message']['date']
#         local = time.localtime(time.time())
#         ts = time.asctime(local)
#         print(f"Сообщение от пользователя: {item['message']['from']['first_name']} (id: {item['message']['from']['id']}), текст сообщения: {item['message']['text']}, время: {ts}")


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()



def play_game(user_id, text):
    e = 3
    while e > 0:
        send_message(user_id, text)


# задаем вопрос загадай
# после ответа 1 должен еще раз угадай
# после ответа 2 еще раз угадай
# после ответа 3  вывести результат

def check_updates():
    while True:
        updates = get_updates()
        t = time.time()
        if updates['result']:
            for item in updates['result']:
                if int(t) < item['message']['date'] + 1:
                    if item['message']['text'] == 'сыграем':
                        play_game(item['message']['from']['id'], 'угадай число от 1 до 3')
                    # print(f"Сообщение от пользователя: {item['message']['from']['first_name']}, текст сообщения: {item['message']['text']} время: {item['message']['date']} {int(t)}")
        time.sleep(1)  # Задержка в 1 секунду
check_updates()

