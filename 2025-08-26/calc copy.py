import os
from datetime import datetime

class Calc:

    def __init__(self, logger):
        self.logger = logger

    def add(self, number_1, number_2):
        res = number_1 + number_2
        print(res)
        self.logger.log(number_1, number_2, res, '+')

    def substract(self, number_1, number_2):
        res = number_1 - number_2
        print(res)
        self.logger.log(number_1, number_2, res, '-')
        

class SuperClass(Calc):
    def find_percent(self, number, percent):
        res = number * percent / 100
        print(res)
        self.logger.log(number, percent, res, '%')

class Logger():

    def __init__(self, filename):
        self.filename = filename

    def log(self, number_1, number_2, res, action):
        """Запись лога"""
        if os.path.exists(self.filename):
            open_mode = 'a'
        else:
            open_mode = 'w'
        with open(self.filename, open_mode, encoding='utf-8') as f:
            data = f'{datetime.now()}: {number_1} {action} {number_2} = {res}\n'
            f.write(data)

logger = Logger('2025-08-26\\log.txt')

calc = SuperClass(logger)
calc.find_percent(150, 30)