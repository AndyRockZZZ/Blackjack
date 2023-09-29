import time
from cards import Card
from player import Player
from tkinter import Tk, Canvas, Label, Button, PhotoImage, Text
from PIL import ImageTk, Image

deck = Card()
dealer = Player()
player = Player()
game_round = 1
player_ended = False
window = Tk()


def hide_welcome_page():
    print("Removing Welcome Page")
    components = [welcome, message, no_button]
    for component in components:
        component.grid_forget()


def draw_cards(carddeck, playercard, count):
    for i in range(count):
        playercard.draw_card(carddeck.deck)


def hide_gameplay():
    components = [dealer_canvas, dealer_label, dealer_score, player_canvas, player_label, player_score, hit_button,
                  stand_button, info, round_label]
    for component in components:
        component.place_forget()


def show_gameplay():
    components = [dealer_canvas, dealer_label, dealer_score, player_canvas, player_label, player_score, hit_button,
                  stand_button, info, round_label]
    hide_welcome_page()
    time.sleep(2)
    for component in components:
        print(component.place_info())


def sort_score(player1hand):
    for card in player1hand.hand:
        if "Ace" in card:
            player1hand.score -= 10


def player_hit():
    print("Player Hit")
    hit_button["state"] = "disabled"
    stand_button["state"] = "disabled"
    draw_cards(deck, player, 1)
    player_hand_count = len(player.hand)
    info.config(text=f"The player hits, and draws - {player.hand[player_hand_count - 1]}", wraplength=350)
    player.score = deck.get_score(player.hand, False)
    if player.score > 21 and player.has_ace():
        sort_score(player)
    display_hand(player, dealer)
    window.after(2000, func=gameplay)


def player_stand():
    global player_ended
    player_ended = True
    info.config(text="The player stands")
    window.after(1000, func=gameplay)

def play_game():
    global player_ended
    play_again_button.config(text="Play again")
    play_again_button["state"] = "disabled"
    stop_play_button["state"] = "disabled"
    dealer.clear_hand()
    player.clear_hand()
    player_ended = False
    gameplay()

def stop_game():
    window.quit()

def options():
    info.config(text='If you want to play again, press "Play Again" button. Else press "Stop" button.')
    play_again_button["state"] = "normal"
    stop_play_button["state"] = "normal"


# -------------------------------- Design ------------------------------------- #
window.title("Blackjack")
window.config(width=1000, height=600, bg="green")
blank = ImageTk.PhotoImage(Image.new(mode="RGB", size=(72, 96), color="green"))

# Dealer

dealer_canvas = Canvas(width=400, height=200, bg="green")
dealer1 = dealer_canvas.create_image(50, 100, image=blank)
dealer2 = dealer_canvas.create_image(125, 100, image=blank)
dealer3 = dealer_canvas.create_image(200, 100, image=blank)
dealer4 = dealer_canvas.create_image(275, 100, image=blank)
dealer5 = dealer_canvas.create_image(350, 100, image=blank)
dealer_canvas.place(x=275, y=10)

dealer_label = Label(text="Dealer", font=("Arial", 25), bg="green", fg="Yellow")
dealer_label.place(x=710, y=10)
dealer_score = Label(text="Score = 0", font=("Arial", 20), bg="green", fg="Yellow")
dealer_score.place(x=710, y=50)

# Player

player_canvas = Canvas(width=400, height=200, bg="green")
player1 = player_canvas.create_image(50, 100, image=blank)
player2 = player_canvas.create_image(125, 100, image=blank)
player3 = player_canvas.create_image(200, 100, image=blank)
player4 = player_canvas.create_image(275, 100, image=blank)
player5 = player_canvas.create_image(350, 100, image=blank)
player_canvas.place(x=275, y=390)

player_label = Label(text="Player", font=("Arial", 25), bg="green", fg="Yellow")
player_label.place(x=710, y=400)
player_score = Label(text="Score = 0", font=("Arial", 20), bg="green", fg="Yellow")
player_score.place(x=710, y=440)

# Other
hit_button = Button(text="Hit", font=("Arial", 20), width=10, height=2, bg="red", command=player_hit)
hit_button["state"] = "disabled"
hit_button.place(x=105, y=255)

stand_button = Button(text="Stand", font=("Arial", 20), width=10, height=2, bg="cyan", command=player_stand)
stand_button["state"] = "disabled"
stand_button.place(x=680, y=255)

info = Label(window, text='If you want to play, press the "Play" button. If not either press "Stop" or the exit button.', font=("Arial", 16), wraplength=350)
info.place(x=300, y=250, width=350, height=100)

round_label = Label(text=f"Round: {game_round}", font=("Arial", 16), bg="green", fg="yellow")
round_label.place(x=10, y=10)

deck_size_label = Label(text=f"Deck Size: {deck.deck_size()}", font=("Arial", 16), bg="green", fg="yellow")
deck_size_label.place(x=120, y=10)

play_again_button = Button(text="Play", font=("Arial", 12), width=10, height=1, bg="Yellow", command=play_game)
play_again_button.place(x=10, y=50)

stop_play_button = Button(text="Stop", font=("Arial", 12), width=10, height=1, bg="Yellow", command=stop_game)
stop_play_button.place(x=120, y=50)

"""
# Welcome Screen

welcome = Label(text="Welcome to Blackjack", font=("Arial", 40), bg="green", fg="Yellow")
welcome.grid(column=1, row=0)

message = Label(text="Would you like to play a game?", font=("Arial", 24), bg="green", fg="Yellow")
message.grid(column=1, row=1)

no_button = Button(text="No", font=("Arial", 12), bg="red", width=10, height=2)
no_button.grid(column=2, row=2)

yes_button = Button(text="Yes", font=("Arial", 12), bg="cyan", width=10, height=2, command=show_gameplay)
yes_button.grid(column=0, row=2)
"""


# ---------------------------- Gameplay ------------------------------------------------------#

def compare_score(player1score, player2score):
    if player1score.score > 21:
        info.config(text="You went bust, you lose.")
    elif player1score.score <= 21 and player2score.score > 21:
        info.config(text="The dealer went bust, you win.")
    else:
        if player1score.score > player2score.score:
            info.config(text="You win.")
        elif player1score.score < player2score.score:
            info.config(text="You lose.")
        else:
            info.config(text="It's a draw.")
    window.after(7000, func=options)

def display_hand(player, dealer):
    global player_ended
    dealers_hand_length = len(dealer.hand)
    players_hand_length = len(player.hand)
    dealer_card_order = [dealer1, dealer2, dealer3, dealer4, dealer5]
    player_card_order = [player1, player2, player3, player4, player5]
    dealer.hand_images = []
    player.hand_images = []

    for card in range(dealers_hand_length):
        card_image = PhotoImage(file=f"./cardImages/{dealer.hand[card]}.png")
        if card == 1 and dealers_hand_length == 2 and not player_ended:
            card_image = PhotoImage(file=f"./cardImages/BackFace.png")
        if card_image not in dealer.hand_images:
            dealer.hand_images.append(card_image)
        dealer_canvas.itemconfig(dealer_card_order[card], image=dealer.hand_images[card])
    dealer_score.config(text=f"Score = {dealer.score}")

    for card in range(players_hand_length):
        card_image = PhotoImage(file=f"./cardImages/{player.hand[card]}.png")
        if card_image not in player.hand_images:
            player.hand_images.append(card_image)
        player_canvas.itemconfig(player_card_order[card], image=player.hand_images[card])
    player_score.config(text=f"Score = {player.score}")


def dealer_plays():
    dealer.score = deck.get_score(dealer.hand, False)
    if dealer.score > 21 and dealer.has_ace():
        sort_score(dealer)
    print(f"{dealer.score}")
    info.config(text=f"The dealer hits, and draws - {dealer.hand[len(dealer.hand) - 1]}", wraplength=350)
    if dealer.score < 17 and player.score <= 21:
        display_hand(player, dealer)
        draw_cards(deck, dealer, 1)
        dealer.score = deck.get_score(dealer.hand, False)
        print(f"New Card {dealer.hand[len(dealer.hand) - 1]} Score = {dealer.score}")
        window.after(5000, func=dealer_plays)

    else:
        print("Finish")
        display_hand(player, dealer)
        compare_score(player, dealer)

def start_draw():
    draw_cards(deck, player, 2)
    draw_cards(deck, dealer, 2)
    player.score = deck.get_score(player.hand, False)
    dealer.score = deck.get_score(dealer.hand, True)
    display_hand(player, dealer)
    window.after(1000, func=gameplay)


def gameplay():
    global player_ended, game_round
    round_label.config(text=f"Round: {game_round}")
    deck_size_label.config(text=f"Deck Size: {deck.deck_size()}")
    if deck.deck_size() < 10:
        deck.deck = []
        deck.new_deck()
    if player.hand_count() == 0 and dealer.hand_count() == 0:
        start_draw()
    if player.score == 21 and player.hand_count() == 2:
        player_ended = True

    if player.score >= 21 or player_ended:
        player_ended = True
        info.config(text='The dealer plays')
        hit_button["state"] = "disabled"
        stand_button["state"] = "disabled"
        window.after(2000, func=dealer_plays)
        game_round += 1
    else:
        info.config(text='Do you want to "hit" (get another card) or "stand"? Please press one of the buttons.')
        hit_button["state"] = "normal"
        stand_button["state"] = "normal"


window.mainloop()
