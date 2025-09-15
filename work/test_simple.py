from chromadb import HttpClient, PersistentClient
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import time

print("Тест простого подключения...")

# Пробуем in-memory базу сначала
try:
    from chromadb import Client
    client = Client(Settings(anonymized_telemetry=False))
    collection = client.create_collection("test_collection")
    collection.add(ids=["1"], documents=["test document"])
    results = collection.query(query_texts=["test"], n_results=1)
    print("✅ In-memory база работает")
except Exception as e:
    print(f"❌ In-memory ошибка: {e}")

# Тест с PersistentClient с таймаутом
print("Тест PersistentClient...")
try:
    client = PersistentClient(
        path="./test_db",
        settings=Settings(anonymized_telemetry=False, allow_reset=True)
    )
    collection = client.create_collection("test_collection")
    collection.add(ids=["1"], documents=["test document"])
    results = collection.query(query_texts=["test"], n_results=1)
    print("✅ PersistentClient работает")
except Exception as e:
    print(f"❌ PersistentClient ошибка: {e}")