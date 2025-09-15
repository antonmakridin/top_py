import requests
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Конфигурация
YC_API_KEY = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
YC_FOLDER_ID = 'b1goak37d5prthkdfd7n'
CSV_FILE_PATH = "D:\\work\\TOP\\html\\top_py\\work\\chroma.csv"

print("🚀 Запуск чат-бота с вашей базой CSV...")

# 1. Загрузка данных из CSV
print(f"📂 Загрузка данных из {CSV_FILE_PATH}...")
try:
    df = pd.read_csv(CSV_FILE_PATH, sep=';ASOD;')
    print(f"✅ Файл загружен. Столбцы: {list(df.columns)}")
    
    # Проверяем наличие нужных столбцов
    if 'question' not in df.columns or 'answer' not in df.columns:
        print("❌ В CSV файле должны быть столбцы 'question' и 'answer'")
        exit()
    
    questions = df['question'].tolist()
    answers = df['answer'].tolist()
    
    print(f"📊 Загружено {len(questions)} вопросов и {len(answers)} ответов")
    
    # Убираем пустые значения
    valid_data = []
    for i, (q, a) in enumerate(zip(questions, answers)):
        if pd.notna(q) and pd.notna(a) and str(q).strip() and str(a).strip():
            valid_data.append((str(q).strip(), str(a).strip()))
        else:
            print(f"⚠️  Пропущена пустая запись в строке {i+1}")
    
    if not valid_data:
        print("❌ Нет валидных данных в CSV файле")
        exit()
    
    questions, answers = zip(*valid_data)
    print(f"✅ Обработано {len(questions)} валидных записей")
    
except Exception as e:
    print(f"❌ Ошибка загрузки CSV файла: {e}")
    exit()

# 2. Инициализация модели для эмбеддингов
print("📦 Загрузка модели для эмбеддингов...")
try:
    embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    print("✅ Модель загружена")
except Exception as e:
    print(f"❌ Ошибка загрузки модели: {e}")
    exit()

# 3. Создаем простую базу данных в памяти
class SimpleVectorDB:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.embeddings = None
        
    def add_data(self, questions, answers, batch_size=100):
        self.questions = list(questions)
        self.answers = list(answers)
        
        print("🔨 Создание эмбеддингов...")
        print(f"📈 Обработка {len(questions)} записей...")
        
        # Обрабатываем батчами для избежания переполнения памяти
        all_embeddings = []
        for i in range(0, len(questions), batch_size):
            batch_end = min(i + batch_size, len(questions))
            batch_questions = questions[i:batch_end]
            
            print(f"   Обрабатывается батч {i//batch_size + 1}/{(len(questions)-1)//batch_size + 1} ({batch_end-i} записей)")
            
            batch_embeddings = embedder.encode(batch_questions, show_progress_bar=False)
            all_embeddings.append(batch_embeddings)
        
        self.embeddings = np.vstack(all_embeddings)
        print(f"✅ Добавлено {len(questions)} вопросов-ответов")
        print(f"📊 Размерность эмбеддингов: {self.embeddings.shape}")
        
    def search(self, query, top_k=5):
        query_embedding = embedder.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Получаем индексы самых похожих результатов
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                'question': self.questions[idx],
                'answer': self.answers[idx],
                'similarity': similarities[idx]
            })
        return results

# 4. Создаем и наполняем базу данных
print("🗄️ Создание базы знаний...")
db = SimpleVectorDB()
db.add_data(questions, answers)

# 5. Функция поиска
def search_relevant_answers(user_query, top_k=2):
    print(f"🔍 Поиск ответов для: '{user_query}'")
    results = db.search(user_query, top_k)
    
    relevant_contexts = []
    print("📋 Найденные результаты:")
    
    for i, result in enumerate(results):
        print(f"   {i+1}. [схожесть: {result['similarity']:.3f}] В: {result['question']} | О: {result['answer']}")
        context_item = f"Вопрос: {result['question']}\nОтвет: {result['answer']}"
        relevant_contexts.append(context_item)
    
    return relevant_contexts

# 6. Функция запроса к YandexGPT
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
                    "text": (
                        "Ты - помощник, основанный на собственной базе знаний. "
                        "Отвечай на вопрос пользователя ТОЛЬКО на основе предоставленного контекста ниже. "
                        "Если ответа нет в контексте, вежливо скажи, что не знаешь ответа. "
                        "Не придумывай ничего от себя. "
                        f"Контекст:\n{context}"
                    )
                },
                {
                    "role": "user",
                    "text": user_question
                }
            ]
        }

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {YC_API_KEY}",
            "x-folder-id": YC_FOLDER_ID
        }

        print("🤖 Запрос к YandexGPT...")
        response = requests.post(url, headers=headers, json=prompt, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        # Проверяем структуру ответа
        if 'result' in result and 'alternatives' in result['result']:
            if result['result']['alternatives']:
                return result['result']['alternatives'][0]['message']['text']
            else:
                return "Не получилось сгенерировать ответ"
        else:
            return f"Неожиданный формат ответа: {result}"
        
    except requests.exceptions.RequestException as e:
        return f"❌ Ошибка сети: {str(e)}"
    except Exception as e:
        return f"❌ Ошибка при запросе к YandexGPT: {str(e)}"

# 7. Главная функция бота
def chat_bot(user_query):
    print("\n" + "="*60)
    print(f"💬 Вопрос: {user_query}")
    
    # Ищем релевантные ответы
    relevant_contexts = search_relevant_answers(user_query)
    
    if not relevant_contexts:
        return "К сожалению, не нашлось подходящей информации в базе знаний."
    
    # Объединяем в контекст
    context_text = "\n\n".join(relevant_contexts)
    print(f"📄 Контекст подготовлен ({len(context_text)} символов)")
    print(f"📝 Контекст: {context_text[:200]}...")  # Покажем начало контекста для отладки
    
    # Отправляем в YandexGPT
    answer = ask_yandex_gpt(context_text, user_query)
    
    if answer is None:
        return "Не удалось получить ответ от YandexGPT"
    
    return answer

# 8. Интерактивный режим
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🤖 Чат-бот готов к работе!")
    print("💡 Введите ваш вопрос или 'выход' для завершения")
    print("="*60)
    
    while True:
        try:
            user_input = input("\n👤 Ваш вопрос: ").strip()
            
            if user_input.lower() in ['выход', 'exit', 'quit', 'q']:
                print("👋 До свидания!")
                break
                
            if not user_input:
                print("⚠️  Пожалуйста, введите вопрос")
                continue
                
            answer = chat_bot(user_input)
            print(f"\n🤖 Ответ: {answer}")
            
        except KeyboardInterrupt:
            print("\n👋 До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")