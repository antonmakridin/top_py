import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import numpy as np

# Конфигурация
YC_API_KEY = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
YC_FOLDER_ID = 'b1goak37d5prthkdfd7n'

print("Инициализация Qdrant...")

# Используем in-memory Qdrant для простоты
client = QdrantClient(":memory:")
embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Создаем коллекцию
client.recreate_collection(
    collection_name="qa_collection",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

# Добавляем тестовые данные
test_data = [
    {"question": "Какая кость не прикреплена к другой кости", "answer": "Подъязычная кость"},
    {"question": "Как работает сердце человека", "answer": "Сердце качает кровь по сосудам"},
    {"question": "Что такое ДНК", "answer": "Дезоксирибонуклеиновая кислота, носитель генетической информации"}
]

points = []
for i, item in enumerate(test_data):
    embedding = embedder.encode(item["question"]).tolist()
    points.append(
        PointStruct(
            id=i,
            vector=embedding,
            payload={"question": item["question"], "answer": item["answer"]}
        )
    )

client.upsert(collection_name="qa_collection", points=points)
print(f"✅ База создана: {len(test_data)} записей")

def search_relevant_answers(user_query, top_k=3):
    try:
        query_embedding = embedder.encode(user_query).tolist()
        
        results = client.search(
            collection_name="qa_collection",
            query_vector=query_embedding,
            limit=top_k
        )
        
        relevant_answers = []
        for result in results:
            relevant_answers.append(result.payload["answer"])
            print(f"Найден: {result.payload['question']} (score: {result.score:.3f})")
        
        return relevant_answers
        
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return []

def ask_yandex_gpt(context, user_question):
    try:
        prompt = {
            "modelUri": f"gpt://{YC_FOLDER_ID}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.1,
                "maxTokens": 2000
            },
            "messages": [
                {
                    "role": "system",
                    "text": f"Отвечай только на основе контекста: {context}"
                },
                {"role": "user", "text": user_question}
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {YC_API_KEY}",
            "x-folder-id": YC_FOLDER_ID
        }

        response = requests.post(
            "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
            headers=headers,
            json=prompt,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result['result']['alternatives'][0]['message']['text']
        
    except Exception as e:
        return f"Ошибка YandexGPT: {e}"

# Тестируем
user_question = "Расшифруй ДНК"
print(f"\nВопрос: {user_question}")

answers = search_relevant_answers(user_question)
if answers:
    context = "\n".join(answers)
    response = ask_yandex_gpt(context, user_question)
    print(f"\nОтвет: {response}")
else:
    print("Не найдено ответов")