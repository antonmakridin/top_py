import requests
import json
import os

url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

API_TOKEN = 'dsanS6I9eho5'
CATALOG = 'b1sk37d7n'

class DB:
    def __init__(self, filename):
        self.filename = filename

    def add_translate(self, text, language, result):
        texts = self.read()
        texts.append(f"{text}\nперевод на {language} - {result}")
        self.write(texts)
    
    def write(self, texts):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(texts, f, ensure_ascii=False)
    
    def read(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

def get_answer(text, language):
    translate = f"Переведи текст на {language}: {text}"
    data = {
        "modelUri": f"gpt://{CATALOG}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.4,
            "maxTokens": 100,
            "reasoningOptions": {
                "mode": "DISABLED"
            }
        },
        "messages": [
            {
                "role": "user",
                "text": translate,
            }
        ]
    }

    headers = {'Authorization': f"Api-Key {API_TOKEN}"}
    
    try:
        res = requests.post(url, json=data, headers=headers, timeout=10)
        res.raise_for_status()
        return res.json()['result']['alternatives'][0]['message']['text']
    except requests.exceptions.RequestException:
        return "Ошибка подключения к API"
    except (KeyError, IndexError):
        return "Ошибка обработки ответа"
    
# Экземпляр класса базы данных
db = DB('2025-08-29\\translate.json')
while True:
    lang = input('Введи язык для перевода: ').strip()
    if not lang:
        continue
        
    user = input('Введи текст для перевода: ').strip()
    if not user:
        continue
        
    result = get_answer(user, lang)
    print(f'Перевод: {result}')
    
    db.add_translate(user, lang, result)
    print('s')