class Microwave():
    def __init__(self):
        self.min_power = 1
        self.max_power = 800
        self.min_timer = 1
        self.max_timer = 30
        self.timer = 0
        self.power = 0
        self.pow = False
        self.time = False

    def set_power(self, pow):
        if self.min_power < pow <= self.max_power:
            self.power = pow
            print(f'Мощность установлена на  {self.power} Вт')
            self.pow = True
        else:
            print(f'Ошибка: мощность должна быть в диапазоне {self.min_power}-{self.max_power} Вт')

    def set_timer(self, time):
        if self.min_timer < time <= self.max_timer:
            self.timer = time
            print(f'Таймер установлен на {self.timer} минут')
            self.time = True
        else:
            print(f'Ошибка: таймер должен быть в диапазоне {self.min_timer}-{self.max_timer} минут')
    
    def heat(self):
        if self.pow and self.time:
            print(f'Микроволновка разогревает еду {self.timer} минут при мощности {self.power} Вт \nРазогрев завершён')
        elif self.pow and not self.time:
                print(f'Нельзя начать: время = {self.timer}')
        elif self.time and not self.pow:
                print(f'Нельзя начать: мощность = {self.power}')

mw = Microwave() 
mw.set_power(600) # Мощность установлена на 600 Вт 
mw.set_timer(5) # Таймер установлен на 5 минут 
mw.heat() # Микроволновка разогревает еду 5 минут при мощности 600 Вт # Разогрев завершён # Ошибочные ситуации 
mw.set_power(1000)
# Ошибка: мощность должна быть в диапазоне 0–800 Вт 
mw.set_timer(40) # Ошибка: таймер должен быть в диапазоне 1–30 минут 
mw2 = Microwave()
mw2.set_timer(20)
mw2.heat() # Нельзя начать: мощность = 0