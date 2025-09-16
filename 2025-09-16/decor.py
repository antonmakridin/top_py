def check_user(function_name):
    def func(name):
        print('проверяем имя')
        print('вызываем исходную функцю')
        if name != 'Боб':
            return function_name(name)
        else:
            print('кажется ты Боб')
    return func

@check_user
def hello(name):
    print(f'привет {name}!')
    
@check_user
def bye(name):
    print(f'пока {name}')

hello = check_user(hello)
hello('Алиса')
hello('Боб')