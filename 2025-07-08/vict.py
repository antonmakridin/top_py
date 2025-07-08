import random

rand_num = random.randint(1, 3)
print(rand_num)
print('Угадай число от 1 до 3')
for i in range(3):
    num = int(input('Число: '))
    if num == rand_num:
        print('Угадал')
        break