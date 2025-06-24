# #1
# users = [
#     {"id": 1, "name": "Alice", "age": 25, "status": "active"},
#     {"id": 2, "name": "Bob", "age": 30, "status": "inactive"},
#     {"id": 3, "name": "Charlie", "age": 35, "status": "active"},
#     {"id": 4, "name": "David", "age": 20, "status": "pending"}
# ]
# #активные пользователей
# active_users = [user["name"] for user in users if user["status"] == "active"]
# #средний возраст всех
# avg_age = sum(user["age"] for user in users) / len(users)
# #минимальный возраст пользователя
# min_active_age = min(user["age"] for user in users if user["status"] == "active")
# #создаем полученный словарь
# result = {
#     "active_users": active_users,
#     "avg_age": avg_age,
#     "min_age": min_active_age
# }
# #выводим на экран
# print(result)


#2
users = [
    {"id": 1, "name": "Alice", "age": 25, "status": "active"},
    {"id": 2, "name": "Bob", "age": 30, "status": "inactive"},
    {"id": 3, "name": "Charlie", "age": 35, "status": "active"},
    {"id": 4, "name": "David", "age": 20, "status": "pending"}
]

while True:
    active_users = [user["name"] for user in users if user["status"] == "active"]
    avg_age = sum(user["age"] for user in users) / len(users) if users else 0
    active_ages = [user["age"] for user in users if user["status"] == "active"]
    min_active_age = min(active_ages) if active_ages else 0
    current_stats = {
        "active_users": active_users,
        "avg_age": avg_age,
        "min_age": min_active_age
    }
    print("\nТекущие данные:")
    print(current_stats)
    print("\nМеню:")
    print("1 - Добавить нового пользователя")
    print("2 - Деактивировать пользователя")
    print("3 - Выйти из программы")
    choice = input("Выберите действие (1|2|3): ")
    if choice == "1":
        name = input("Введите имя нового пользователя: ")
        age = int(input("Введите возраст нового пользователя: "))
        # Автоматическая генерация ID
        if users:
            new_id = max(user["id"] for user in users) + 1
        else:
            new_id = 1
        users.append({
            "id": new_id,
            "name": name,
            "age": age,
            "status": "active"
        })
        print(f"Пользователь {name} успешно добавлен!")
    elif choice == "2":
        name_to_deactivate = input("Введите имя пользователя для деактивации: ")
        user_found = False
        for user in users:
            if user["name"] == name_to_deactivate:
                user["status"] = "inactive"
                print(f"Пользователь {name_to_deactivate} деактивирован.")
                user_found = True
                break
        if not user_found:
            print(f"Пользователь с именем {name_to_deactivate} не найден.")
    elif choice == "3":
        print("Выход из программы...")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")