import os
import random

# Укажите путь к вашей папке
folder_path = '2025-09-12\\img'
if os.path.isdir(folder_path):
    # Получаем список всех файлов в папке
    all_files = os.listdir(folder_path)

    # Фильтруем список, оставляя только файлы с расширением .jpg
    jpg_files = [f for f in all_files if f.endswith('.jpg')]

    # Выбираем случайный файл из списка jpg-файлов
    if jpg_files: # Проверяем, что список не пуст
        random_jpg_file = random.choice(jpg_files)
        print(f"Случайный файл .jpg: {random_jpg_file}")
    else:
        jpg_file = '2025-09-12\\nophoto.jpg'
        print(f"несл файл {jpg_file} ")
else:
    print('нет папки')