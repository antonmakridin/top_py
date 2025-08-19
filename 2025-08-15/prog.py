class Programmer:

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.oklad = 10
        self.hours = 0
        self.summa = 0
        self.oklad_junior = 10
        self.oklad_middle = 15
        self.oklad_senior = 20
        self.bonus = 1

    def rise(self):
        if self.title == 'Junior':
            self.title = 'Middle'
            self.oklad = self.oklad_middle
        elif self.title == 'Middle':
            self.title = 'Senior'
            self.oklad = self.oklad_senior
        else:
            self.oklad += self.bonus

    def work(self, hours):
        self.hours += hours
        if self.title == 'Junior':
            self.summa += hours * self.oklad
        elif self.title == 'Middle':
            self.summa += hours * self.oklad
        elif self.title == 'Senior':
            self.summa += hours * self.oklad
    
    def info(self):
        print(f'{self.name} {self.hours}ч. {self.summa}тгр.')

        
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
programmer.info()
programmer.rise()
programmer.work(500)
programmer.info()
programmer.rise()
programmer.work(250)
programmer.info()
programmer.rise()
programmer.work(250)
programmer.info()
programmer.rise()
programmer.work(250)
programmer.info()