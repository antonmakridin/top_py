class RedButton:

    def __init__(self):
        self.kolvo = 0

    def click(self):
        print('Тревога!')
        self.kolvo += 1

    def count(self):
        return self.kolvo

first_button = RedButton()
first_button.click()
first_button.click()
print(first_button.count())