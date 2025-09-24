# #1
# q_dict = {
#     "Столица Франции?": "Париж",
#     "2 + 2?": "4",
#     "Какой цвет получается при смешивании синего и жёлтого?": "Зелёный"
# }
# # Выводим вопросы
# print("Список вопросов:")
# for question in q_dict.keys():
#     print(question)
# # Выводим ответы
# print("\nСписок ответов:")
# for answer in q_dict.values():
#     print(answer)
# # Выводим пары вопрос - ответ
# print("\nПары вопрос - ответ:")
# for question, answer in q_dict.items():
#     print(f"{question} - {answer}")

# #2
# q_dict = {
#     "Столица Франции?": "Париж",
#     "2 + 2?": "4",
#     "Какой цвет получается при смешивании синего и жёлтого?": "Зелёный"
# }
# score = 0  # Счетчик правильных ответов
# print("Ответьте на вопросы:\n")
# # Задаем каждый вопрос и проверяем ответ
# for question, correct_answer in q_dict.items():
#     user_answer = input(question + " ").strip()  # Получаем ответ пользователя
#     if user_answer.lower() == correct_answer.lower():
#         print("Верно!")
#         score += 1
#     else:
#         print(f"Неправильно. Правильный ответ: {correct_answer}")
# # Выводим итоговый результат
# print(f"\nВаш результат: {score} из {len(q_dict)}")


# #3
# dictionary = {
#     "mork": "кот",
#     "brel": "бежит",
#     "drun": "по",
#     "plek": "дороге"
# }
# fake_sentence = "mork brel drun plek"
# # Разбиваем строку на слова
# words = fake_sentence.split()
# # Переводим каждое слово, используя dictionary
# translated_words = [dictionary[word] for word in words]
# # Собираем слова в предложение
# russian_sentence = ' '.join(translated_words)
# print(russian_sentence)


#4
string = input("Введите строку: ")
# Разбиваем строку
word_length_dict = {word: len(word) for word in string.split()}
# Выводим результат
print(f"{string} {word_length_dict}")