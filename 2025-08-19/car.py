class Car():
    def __init__(self, color, fuel, rate):
        self.color = color
        self.fuel = fuel
        self.rate = rate
        self.mileage = 0

    def drive(self, distance):
        need_fuel = self.rate * distance / 100
        if need_fuel <= self.fuel:
            print(f'Проехали {distance} км')
            self.fuel = self.fuel - need_fuel
            print(f'Осталось топлива {self.fuel} км')
            self.mileage += distance
        else:
            max_distance = self.fuel * 100 / self.rate
            print(f'Не хватает топлива. Хватит только на {max_distance} км.')

    def get_mileage(self):
            print(f'Пробег {self.mileage} км')

car = Car('Черный', 50, 5)
car.drive(5000)
car.drive(500)
car.drive(50)
car.get_mileage()