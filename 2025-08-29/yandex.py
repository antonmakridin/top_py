import requests

url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

API_TOKEN = 'AQVNwEo4xD0so5'
CATALOG = 'b1gdn'

def get_answer(text):
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
                "text": text,
            },
            {
                "role": "user",
                "text": 'отвечай поэтично',
            }
        ]
    }

    headers = {'Authorization': f"Api-Key {API_TOKEN}"}
    res = requests.post(url, json=data, headers=headers)
    print(res.text)
    return res.json()['result']['alternatives'][0]['message']['text']

while True:
    user = input('Введи запрос: ')
    print(get_answer(user))