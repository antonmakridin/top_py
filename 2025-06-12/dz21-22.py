# #1
# cities = {
#     "Екатеринбург": 1548187,
#     "Москва": 13200000,
#     "Санкт-Петербург": 5400000,
#     "Новосибирск": 1650000
# }
# for city, population in cities.items():
#     print(f"Город: {city}, Население: {population:,} ч".replace(',', ' '))


# #2
# cities = {}
# for _ in range(3):
#     city = input("Введите название города: ")
#     population = int(input("Введите количество жителей: "))
#     cities[city] = population
# print("\nИнформация о городах:")
# for city, population in cities.items():
#     print(f"Город: {city}, Население: {population:,} ч".replace(',', ' '))


# #3
# words = 'это секретное сообщение'
# cipher = {'это': 1, 'сообщение': 2, 'секретное': 4}
# word_list = words.split()
# encoded_message = [str(cipher.get(word, word)) for word in word_list]
# result = ''.join(encoded_message)
# print("Результат:", result)


#4
students = {
    'Аня': [5, 4, 5],
    'Борис': [3, 2, 3],
    'Вика': [4, 4, 4],
    'Дима': [2, 2, 3]
}
print("Средние оценки студентов:")
averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"{name}: {avg}")
best_student = None
highest_avg = 0
for name, avg in averages.items():
    if avg > highest_avg:
        highest_avg = avg
        best_student = name
print(f"\nСтудент с самой высокой средней оценкой: {best_student} ({highest_avg})")
students_with_2 = []
for name, grades in students.items():
    if 2 in grades:
        students_with_2.append(name)
print("\nСтуденты с хотя бы одной оценкой 2:", ", ".join(students_with_2))