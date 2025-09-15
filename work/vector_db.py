import requests
import json
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import traceback

# Конфигурация
YC_API_KEY = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
YC_FOLDER_ID = 'b1goak37d5prthkdfd7n'
CHROMA_DB_PATH = "D:\\work\\TOP\\html\\top_py\\work\\chroma_db_qa"

print("Инициализация модели эмбеддингов...")
embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

print("Подключение к ChromaDB...")
try:
    client = PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_collection(name="qa_collection")
    print(f"Коллекция загружена. Записей: {collection.count()}")
except Exception as e:
    print(f"Ошибка подключения к коллекции: {e}")
    exit()

def search_relevant_answers(user_query, top_k=3):
    try:
        print(f'Поиск для: "{user_query}"')
        
        # Создаем эмбеддинг
        embedding = embedder.encode([user_query])
        print(f"Эмбеддинг создан. Размер: {embedding.shape}")
        
        query_embedding = embedding.tolist()
        
        # Поиск в базе
        print("Выполняем запрос к ChromaDB...")
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
            include=["metadatas", "distances", "documents"]
        )
        
        print("Запрос выполнен успешно")
        
        # Обработка результатов
        relevant_answers = []
        if results['metadatas'] and len(results['metadatas']) > 0:
            for i, metadata in enumerate(results['metadatas'][0]):
                relevant_answers.append(metadata['answer'])
                print(f"Результат {i+1}: distance={results['distances'][0][i]:.4f}")
        
        return relevant_answers
        
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        traceback.print_exc()
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
                    "text": f"Ты - помощник, основанный на собственной базе знаний. Отвечай ТОЛЬКО на основе контекста: {context}"
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
        return f"Ошибка при запросе к YandexGPT: {e}"

def chat_bot(user_query):
    print("Обработка запроса...")
    relevant_answers = search_relevant_answers(user_query)
    
    if not relevant_answers:
        return "Не удалось найти相关信息 в базе знаний."
    
    context_text = "\n\n".join(relevant_answers)
    print(f"Контекст подготовлен ({len(context_text)} символов)")
    
    answer = ask_yandex_gpt(context_text, user_query)
    return answer

# Тестовый запрос
if __name__ == "__main__":
    user_question = "Какая кость не прикреплена к другой кости в организме"
    print(f"Вопрос: {user_question}")
    
    bot_answer = chat_bot(user_question)
    print(f"Ответ бота: {bot_answer}")