import pandas as pd
from chromadb import PersistentClient
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Конфигурация
CSV_FILE_PATH = "D:\\work\\TOP\\html\\top_py\\work\\chroma.csv"  # Путь к вашему файлу с вопросами-ответами
CHROMA_DB_PATH = "D:\\work\\TOP\\html\\top_py\\work\\chroma_db_qa"  # Папка, где будет храниться векторная БД
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


# if not os.path.exists(CSV_FILE_PATH):
#     print('0')
# else:
#     print('1')
#     df_custom = pd.read_csv(CSV_FILE_PATH, sep=";")

# 1. Загружаем модель для создания эмбеддингов
# При первом запуске модель скачается с Hugging Face (это может занять время)
print("Загрузка модели для эмбеддингов...")
embedder = SentenceTransformer(EMBEDDING_MODEL)

# 2. Загружаем данные из CSV
print("Чтение данных из CSV...")
df = pd.read_csv(CSV_FILE_PATH, sep=";")
# Убедимся, что нет пропущенных значений
df = df.dropna()

# Конвертируем в списки
questions = df['question'].tolist()
answers = df['answer'].tolist()

# 3. Создаем эмбеддинги (векторные представления) для всех вопросов.
# ВАЖНО: Мы индексируем ВОПРОСЫ, чтобы по ним искать.
print(f"Создание эмбеддингов для {len(questions)} вопросов...")
question_embeddings = embedder.encode(questions, show_progress_bar=True, batch_size=32)

# 4. Инициализируем клиент ChromaDB
print("Инициализация ChromaDB...")
client = PersistentClient(path=CHROMA_DB_PATH, settings=Settings(allow_reset=True))

# Создаем коллекцию. Указываем, что размерность векторов равна 384 (размерность выхода выбранной модели).
collection = client.get_or_create_collection(
    name="qa_collection",
    metadata={"hnsw:space": "cosine"}  # Используем косинусное расстояние для определения похожести
)

# 5. Подготавливаем данные для добавления в базу
# ChromaDB ожидает:
# - ids (list[str]): уникальные id для каждой записи
# - embeddings (list[list[float]]): список векторов
# - documents (list[str]): исходные тексты, по которым делались эмбеддинги (в нашем случае вопросы)
# - metadatas (list[dict]): дополнительная информация, которую мы хотим хранить (в нашем случае ОТВЕТЫ)

documents = questions  # Документы - это наши вопросы
embeddings = question_embeddings.tolist()  # Конвертируем numpy array в list of lists
ids = [f"id_{i}" for i in range(len(questions))]  # Генерируем простые ID

# Самое главное: сохраняем ответы в метаданные!
metadatas = [{"answer": answer} for answer in answers]

# 6. Добавляем все данные в коллекцию
print("Добавление данных в векторную базу...")
collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=documents,  # По этому полю можно тоже искать, но мы будем искать по векторам
    metadatas=metadatas  # Здесь хранится наш "сокровищница" - ответы
)

print(f"Готово! В базу добавлено {collection.count()} вопросов-ответов.")