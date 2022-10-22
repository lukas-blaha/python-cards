
class Card:
    def __init__(self):
        self.type = ""
        self.rel_value = ""
        self.value = 0

    def show(self):
        print(f'{self.rel_value} of {self.type} has value: {self.value}')
