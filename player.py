import random

class Player:
    def __init__(self):
        self.hand = []
        self.hand_images = []
        self.score = 0
        self.money = 1000

    def draw_card(self, deck):
        random_card = random.choice(deck)
        self.hand.append(random_card)
        deck.remove(random_card)

    def display_hand(self):
        for hand in self.hand:
            print(hand)

    def hand_count(self):
        return len(self.hand)

    def has_ace(self):
        for card in self.hand:
            if "Ace" in card:
                return True
        return False

    def clear_hand(self):
        self.hand = []
        self.hand_images = []

