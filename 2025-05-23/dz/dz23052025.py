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
# words = ['apple', 'banana', 'cherry']
# # stroka = ''
# # for s in words:
# #     stroka += s
# # print(len(stroka))
# #или
# print(len(''.join(words)))


#3
words = ['apple', 'banana', 'cherry', 'cherry', 'lemon', 'apple']
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)
        print(w, '-', words.count(w))
print(unique_words)