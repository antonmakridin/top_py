# #1
# translations = {
#     "apple": "яблоко",
#     "banana": "банан",
#     "cherry": "вишня"
# }
# for word, translation in translations.items():
#     print(f"Слово: {word}, Перевод: {translation}")


# #2
# products = {}
# for i in range(3):
#     name = input("Введите название товара: ")
#     price = int(input("Введите цену: "))
#     products[name] = price
# print("Словарь цен:", products)


# #3
# capitals = {
#     "Франция": "Париж",
#     "Италия": "Рим",
#     "Германия": "Берлин",
#     "Россия": "Москва"
# }
# for country, capital in capitals.items():
#     while True:
#         user_answer = input(f"Назовите столицу страны {country}: ").strip()
#         if user_answer.lower() == capital.lower():
#             print("Верно!")
#             break
#         else:
#             print(f"Неверно. Попробуйте ещё раз!")


#4
cipher_text = "hfnos"
cipher_map = {
    'h': 'п', 
    'f': 'р', 
    'n': 'и', 
    'o': 'в', 
    's': 'е'
}
decrypted_text = ''.join([cipher_map[char] for char in cipher_text])
print("Расшифрованное слово:", decrypted_text)