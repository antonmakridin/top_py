import os
from chromadb import PersistentClient
from chromadb.config import Settings

# Конфигурация
CHROMA_DB_PATH = "D:\\work\\TOP\\html\\top_py\\work\\chroma_db_qa"

print("=== ДИАГНОСТИКА CHROMADB ===")

# 1. Проверка пути
print(f"1. Проверка пути: {CHROMA_DB_PATH}")
if not os.path.exists(CHROMA_DB_PATH):
    print("   ❌ Путь не существует")
    os.makedirs(CHROMA_DB_PATH, exist_ok=True)
    print("   ✅ Папка создана")
else:
    print("   ✅ Путь существует")

# 2. Проверка содержимого папки
print(f"2. Содержимое папки: {os.listdir(CHROMA_DB_PATH)}")

# 3. Подключение к клиенту
print("3. Подключение к клиенту...")
try:
    client = PersistentClient(
        path=CHROMA_DB_PATH,
        settings=Settings(anonymized_telemetry=False)
    )
    print("   ✅ Клиент подключен")
    
    # 4. Проверка коллекций
    print("4. Проверка коллекций...")
    try:
        collections = client.list_collections()
        print(f"   Найдено коллекций: {len(collections)}")
        for col in collections:
            print(f"   - {col.name}: {col.count()} записей")
            
        # 5. Проверка конкретной коллекции
        print("5. Проверка коллекции 'qa_collection'...")
        try:
            collection = client.get_collection("qa_collection")
            print(f"   ✅ Коллекция найдена: {collection.count()} записей")
            
            # Быстрая проверка поиска
            print("6. Тестовый поиск...")
            try:
                # Простой тест - попробуем найти что-то
                results = collection.peek(limit=1)
                print("   ✅ Поиск работает")
                
            except Exception as e:
                print(f"   ❌ Ошибка поиска: {e}")
                
        except Exception as e:
            print(f"   ❌ Коллекция не найдена: {e}")
            
    except Exception as e:
        print(f"   ❌ Ошибка получения списка коллекций: {e}")
        
except Exception as e:
    print(f"   ❌ Ошибка подключения: {e}")
    import traceback
    traceback.print_exc()

print("=== ДИАГНОСТИКА ЗАВЕРШЕНА ===")