# import json

# name = {
#     "name": "Иван",
#     "age": 30,
#     "is_student": False,
#     "skills": ["Python", "SQL", "Git"]
# }
# # запись в json
# with open('2025-06-27\\users.json', 'w', encoding='utf-8') as f:
#     json.dump(name, f, ensure_ascii=True, indent=4)
# # чтение из json
# with open('2025-06-27\\users.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     print(data)
#     while True:
#         name = [user["name"] for user in data]
#         age = [user["age"] for user in data]
#         is_student = [user["is_student"] for user in data]
#         skills = [user["skills"] for user in data]
#         current_users = {
#             "Имя": name,
#             "Возраст": age,
#             "Студент?": is_student,
#             "Навыки": skills
#         }
#         print("\nТекущие данные:")
#         print(current_users)



import json
# чтение из json
with open('2025-06-27\\db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    u = input('Введи имя пользователя: ')
    p = input('Введи пароль пользователя: ')
    for d in data:
    #выводим на экран
        if u == d['name'] and p == d['password']:
            print('Доступ разрешен')
            for s in d['skills']:
                print(f"skil: {s}")
            break
    else:
        print('Доступ запрещен')



