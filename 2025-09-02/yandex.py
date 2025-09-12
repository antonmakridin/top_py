import requests

class YandexGPT():

    def __init__(self):
        self.token = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
        self.catalog = 'b1goak37d5prthkdfd7n'
        self.url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    def get_answer(self, text, language):
        text = f'Переведи на {language} текст: {text}'
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
