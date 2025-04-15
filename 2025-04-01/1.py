balance = 500
price = 700
money_mode = False

money_code = '123'
code = input('Введи код для денег: ')
if code == money_code:
    money_mode = True


if money_mode:
    print(f'Покупаем, остаток средств: {balance}')
elif balance >= price or money_mode:
    balance -= price
    print(f'Покупаем, остаток средств: {balance}')
else:
    print('Недостаточно денег...')