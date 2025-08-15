class Programmer:

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.oklad = 10
        self.hours = 0
        self.summa = 0

    def rise(self):
        if self.title == 'Junior':
            self.title = 'Middle'
            self.oklad = 15
        elif self.title == 'Middle':
            self.title = 'Senior'
            self.oklad = 20
        else:
            self.oklad += 1

    def work(self, hours):
        self.hours += hours
        if self.title == 'Junior':
            self.summa += hours * self.oklad
        elif self.title == 'Middle':
            self.summa += hours * self.oklad
        elif self.title == 'Senior':
            self.summa += hours * self.oklad
    
    def info(self):
        print(self.name, self.oklad, self.hours, self.summa)

        
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