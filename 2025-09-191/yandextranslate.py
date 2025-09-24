import requests

TOKEN = ''
CATALOG = ''

class YandexGPT():

    def __init__(self):
        self.token = TOKEN
        self.catalog = CATALOG
        self.url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    def get_answer(self, text):
        # text = f'Переведи на {language} текст: {text}'
        data = {
            "modelUri": f"gpt://{self.catalog}/yandexgpt",
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
                }
            ]
        }

        headers = {'Authorization': f"Api-Key {self.token}"}
        res = requests.post(self.url, json=data, headers=headers)
        return res.json()['result']['alternatives'][0]['message']['text']
