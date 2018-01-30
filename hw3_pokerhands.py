# Rofael Aleezada
# January 29 2018
# Pokerhands Program, CS 355
# A program that simulates several instances in a poker game

from random import shuffle
from multiprocessing import Process


# Creates a player with a hand that can draw cards from the top of a deck
class Player:
    hand = None

    def __init__(self):
        self.hand = []

    def __str__(self):
        return self.hand

    def draw_card(self, game_deck):
        card = game_deck.cards.pop(0)
        self.hand.append(card)
        return card


# Creates a deck that generates all standard cards, and can give a specific
# card to a specific player
class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for i in range(10):
            for j in range(i+1):
                self.cards.append(i+1)

    def __str__(self):
        return self.cards

    def give_card(self, player, id_req):
        for i in range(len(self.cards)):
            if self.cards[i] == id_req:
                player.hand.append(self.cards.pop(i))
                break


# Check if a player received a pair
def has_pair(player):
    seen = set()
    for card in player.hand:
        if card in seen:
            return True
        seen.add(card)
    return False

def setup(q3):
    deck = Deck()

    A = Player()
    deck.give_card(A, 6)
    deck.give_card(A, 5)
    deck.give_card(A, 3)
    if q3:
        deck.give_card(A, 10)

    B = Player()
    deck.give_card(B, 10)
    deck.give_card(B, 6)
    deck.give_card(B, 5)

    shuffle(deck.cards)

    return deck, A, B


# Simulate total matches and find when A gets a pair
def a_got_pair(total):
    pairs = 0
    for i in range(total):
        deck, A, _ = setup(False)
        A.draw_card(deck)
        if has_pair(A):
            pairs = pairs + 1
    print("A gets a pair " + str(int(pairs/total * 49)) + "/49 of the time")


# Simulate total matches and find when B gets a pair
def b_got_pair(total):
    pairs = 0
    for i in range(total):
        deck, _, B = setup(False)
        B.draw_card(deck)
        if has_pair(B):
            pairs = pairs + 1
    print("B gets a pair " + str(int(pairs/total * 49)) + "/49 of the time")


# Simulate total matches and find when A draws, doesn't get a pair
# then B draws, gets a pair
def b_got_pair_after_a_got_ten(total):
    pairs = 0
    for i in range(total):
        deck, A, B = setup(True)
        B.draw_card(deck)
        if has_pair(B):
            pairs = pairs + 1
    print("B gets a pair after A draws a 10 " + str(int(pairs/total * 48)) + "/48 of the time")


def run(times):
    p1 = Process(target=a_got_pair, args=[times,])
    p2 = Process(target=b_got_pair, args=[times,])
    p3 = Process(target=b_got_pair_after_a_got_ten, args=[times,])

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


run(10000)
