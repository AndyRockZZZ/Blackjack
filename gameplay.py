from cards import Card
from player import Player
import time

deck = Card()
dealer = Player()
player = Player()
game_round = 0

# --------------------------------------------- Functions --------------------------------------------------------#

def draw_cards(carddeck, playercard, count):
    for i in range(count):
        playercard.draw_card(carddeck.deck)


def compare_score(player1, player2, bid):
    if player1.score > 21:
        print("You went bust, you lose.")
    elif player1.score <= 21 and player2.score > 21:
        print("The dealer went bust, you win.")
        player1.money += bid * 2
    else:
        if player1.score > player2.score:
            print("You win.")
            player1.money += bid * 2
        elif player1.score < player2.score:
            print("You lose.")
        else:
            print("It's a draw.")
            player1.money += bid


def display_hand(player1, player2, all):
    if all:
        print(f"The dealer's hand: {player2.hand}, score: {player2.score}")
    else:
        print(f"The dealer's hand: {player2.hand[0]}, score: {player2.score}")
    print(f"Your hand: {player1.hand}, score: {player1.score}\n")


def display_final_hand(player1, player2):
    print(f"The dealer's final hand: {player2.hand}, final score: {player2.score}")
    print(f"Your final hand: {player1.hand}, final score: {player1.score}\n")


def sort_score(player1):
    for card in player1.hand:
        if player1.score <= 21:
            break;
        else:
            if "Ace" in card:
                player1.score -= 10


# --------------------------------------------- Gameplay --------------------------------------------------------#

print("Welcome to Blackjack\n")
is_ending = False
while not is_ending and player.money != 0:

    if deck.deck_size() < 10:
        deck.deck = []
        deck.new_deck()
    response = input("Would you like to play a game? Y or N: ")
    player.clear_hand()
    dealer.clear_hand()

    if response.upper() == "Y":
        print(f"Your Bank: £{player.money}\n")
        # Set Bid
        bid_complete = False
        while not bid_complete:
            try:
                bid = int(input("Place down your bid: "))
            except ValueError:
                print("You have to enter a numerical value. Enter again")
            else:
                if bid > player.money:
                    print(f"You don't have that much, your current bank is £{player.money}. Enter again.")
                elif bid < 2:
                    print("The minimum bid is £2. Enter again.")
                else:
                    bid_complete = True

        player.money -= bid
        print(f"\nRound {game_round + 1}")
        print(f"You are bidding in £{bid}")
        game_round += 1
        print(f"Deck Size = {deck.deck_size()}\n")
        player_ended = False

        draw_cards(deck, player, 2)
        draw_cards(deck, dealer, 2)
        player.score = deck.get_score(player.hand, False)
        dealer.score = deck.get_score(dealer.hand, False)

        if (player.score == 21 and len(player.hand) == 2) or (dealer.score == 21 and len(dealer.hand) == 2):
            display_final_hand(player, dealer)
            if player.score == 21:
                print("You win, you got Blackjack.")
                player.money += (bid * 2) + (bid * 0.25)
            else:
                print("You lose, the dealer got Blackjack.")
        else:
            dealer.score = deck.get_score(dealer.hand, True)
            while player.score <= 21 and not player_ended:
                display_hand(player, dealer, False)
                hit_or_stand = input('Do you want to "hit" (get another card) or "stand": ')
                if hit_or_stand == "hit":
                    draw_cards(deck, player, 1)
                    player.score = deck.get_score(player.hand, False)
                    if player.score > 21 and player.has_ace():
                        sort_score(player)
                elif hit_or_stand == "stand":
                    player_ended = True
                else:
                    print("Incorrect response, please try again.")
            dealer.score = deck.get_score(dealer.hand, False)
            while dealer.score < 17:
                display_hand(player, dealer, True)
                draw_cards(deck, dealer, 1)
                dealer.score = deck.get_score(dealer.hand, False)
                if dealer.score > 21 and dealer.has_ace():
                    sort_score(dealer)
                time.sleep(5)
            display_final_hand(player, dealer)
            compare_score(player, dealer, bid)
    else:
        is_ending = True
print("\nThank you for playing Blackjack.")
