import os
from datetime import datetime
class Calc:
    def add(self, number_1, number_2):
        res = number_1 + number_2
        print(res)
        self.log(number_1, number_2, res, '+')

    def substract(self, number_1, number_2):
        res = number_1 - number_2
        print(res)
        self.log(number_1, number_2, res, '-')

    def _log(self, number_1, number_2, res, action):
        """Запись лога"""
        filename = "2025-08-26\\log.txt"
        if os.path.exists(filename):
            open_mode = 'a'
        else:
            open_mode = 'w'
        with open(filename, open_mode, encoding='utf-8') as f:
            data = f'{datetime.now()}: {number_1} {action} {number_2} = {res}\n'
            f.write(data)
        


calc = Calc()
calc.substract(3, 4)