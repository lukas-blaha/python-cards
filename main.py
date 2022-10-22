#!/usr/bin/env python3

from deck import Deck
from hand import Hand


def main():
    d = Deck()
    d.shuffle()
    # d.show()
    print(f'There is {len(d.cards)} cards in the deck.')
    print()

    pl1 = Hand()
    pl1.take(d.give(2))
    pl1.show()
    print(f'There is {len(d.cards)} cards in the deck.')

    print()

    pl2 = Hand()
    pl2.take(d.give(2))
    pl2.show()
    print(f'There is {len(d.cards)} cards in the deck.')


main()
