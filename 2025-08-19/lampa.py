class DimmerSwitch:

    def __init__(self):
        self.turn_on = 0
        self.level = 0
        self.maxLevel = 10
        self.minLevel = 0

    def turnOn(self):
        if self.turn_on == 0:
            self.turn_on = 1
            print('Лампа включена')
        else:
            print('Лампа уже включена')
    
    def turnOff(self):
        if self.turn_on == 1:
            self.turn_on = 0
            print('Лампа выключена')
        else:
            print('Лампа уже выключена')

    def raiseLevelUp(self):
        if self.turn_on == 1:
            if self.level < self.maxLevel:
                self.level += 1
            else:
                print('Достигнута максимальная яркость')
        else:
            print('Невозможно увеличить яркость, т.к. лампа выключена!')

    def raiseLevelDown(self):
        if self.turn_on == 1:
            if self.level > self.minLevel:
                self.level -= 1
            else:
                print('Достигнута минимальная яркость')
        else:
            print('Невозможно увеличить яркость, т.к. лампа включена!')
    
    def show(self):
        print(f'Яркость: {self.level}')

        
# Основной код 
dim = DimmerSwitch()
# включаем переключатель и поднимаем уровень яркости 5 раз 
dim.turnOn()
dim.raiseLevelUp()
dim.raiseLevelUp()
dim.raiseLevelUp()
dim.raiseLevelUp()
dim.raiseLevelUp()
dim.show()
dim.turnOff()