
from card import Card
import numpy as np


class Deck:
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        types = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                  "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

        for t in types:
            for i in range(len(values)):
                if i > 9:
                    ni = 10
                else:
                    ni = i+1

                card = Card()
                card.type = t
                card.rel_value = values[i]
                card.value = ni

                self.cards.append(card)

    def show(self):
        for i in range(len(self.cards)):
            self.cards[i].show()

    def shuffle(self):
        np.random.shuffle(self.cards)

    def give(self, n):
        g = []
        for i in range(n):
            g.append(self.cards[0])
            self.cards.pop(0)
        return g
