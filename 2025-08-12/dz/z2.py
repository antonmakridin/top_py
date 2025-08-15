class Dog:
    def __init__(self, name):
        self.dog_name = name
        self.dog_mood = 0

    def talk(self):
        print('гав-гав')

    def walk(self):
        self.dog_mood += 1
        print('Настроение после прогулки:', self.dog_mood)

    def hello(self):
        print('Привет, меня зовут ', self.dog_name)

sobaka = Dog('Бобик')
sobaka.hello() # привет, меня зовут Бобик
sobaka.talk() # гав-гав
sobaka.walk()