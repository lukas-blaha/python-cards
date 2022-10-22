
class Hand:
    def __init__(self):
        self.cards = []

    def take(self, cards):
        for i in range(len(cards)):
            self.cards.append(cards[i])

    def show(self):
        for i in range(len(self.cards)):
            self.cards[i].show()
