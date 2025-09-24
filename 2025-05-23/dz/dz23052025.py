# #1
# data = [[32, 34, 12, 1], [1, 4, 3], [12, 4, 3, 2]]
# res = []
# for d in data:
#     m = d[0]
#     for i in d:
#         if i > m:
#             m = i
#     res.append(m)
# print(res)


# #2
import time
start_time = time.time()  # запоминаем время начала выполнения функции
words = ['apple', 'banana', 'cherry']
for i in range(13):
    words += words
# stroka = ''
# for s in words:
#     stroka += s
# print(len(stroka))
#или
print(len(''.join(words)))
end_time = time.time()  # запоминаем время окончания выполнения функции
execution_time = end_time - start_time  # вычисляем время выполнения функции
print(f"Время выполнения скрипта: {execution_time} секунд")


#3
# words = ['apple', 'banana', 'cherry', 'cherry', 'lemon', 'apple']
# unique_words = []
# for w in words:
#     if w not in unique_words:
#         unique_words.append(w)
#         print(w, '-', words.count(w))
# print(unique_words)