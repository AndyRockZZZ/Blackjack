import random
import math

RANK = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUE = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Card:
    def __init__(self):
        self.deck = []
        self.new_deck()

    def new_deck(self):
        for suit in SUIT:
            for rank in RANK:
                self.deck.append(rank + " of " + suit)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_card_value(self, card):
        split_name = card.split()
        index = RANK.index(split_name[0])
        value = VALUE[index]
        return value

    def get_score(self, players_hand, dealer_start):
        score = 0
        cards = len(players_hand)
        if dealer_start:
            cards = 1
        for card in range(cards):
            if "BackFace" in players_hand[card]:
                break
            score += self.get_card_value(players_hand[card])
        return score

    def deck_size(self):
        return len(self.deck)

    def print_deck(self):
        for card in self.deck:
            print(card)
