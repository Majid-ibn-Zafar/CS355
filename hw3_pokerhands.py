# Rofael Aleezada
# January 29 2018
# Pokerhands Program, CS 355
# A program that simulates several instances in a poker game

from random import shuffle


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


# A card object
class Card:
    type = None

    def __init__(self, typ):
        self.type = typ

    def __str__(self):
        return self.type


# Creates a deck that generates all standard cards, and can give a specific
# card to a specific player
class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for i in range(13):
            if i == 0:
                typ = "A"
            elif i == 10:
                typ = "J"
            elif i == 11:
                typ = "Q"
            elif i == 12:
                typ = "K"
            else:
                typ = str(i + 1)
            for j in range(4):
                self.cards.append(Card(typ))

    def __str__(self):
        return self.cards

    def give_card(self, player, id_req):
        for i in range(len(self.cards)):
            if self.cards[i].type == id_req:
                player.hand.append(self.cards.pop(i))
                break


# Sets up the simulations for this assignment
def setup():
    deck = Deck()

    A = Player()
    deck.give_card(A, "6")
    deck.give_card(A, "5")
    deck.give_card(A, "3")

    B = Player()
    deck.give_card(B, "10")
    deck.give_card(B, "6")
    deck.give_card(B, "5")

    shuffle(deck.cards)

    return deck, A, B


# Check if a player received a pair
def has_pair(player):
    seen = set()
    for card in player.hand:
        card_type = card.type
        if card_type in seen:
            return True
        seen.add(card_type)
    return False


# Simulate total matches and find when A gets a pair
def a_got_pair(total):
    pairs = 0
    for i in range(total):
        deck, A, _ = setup()
        A.draw_card(deck)
        if has_pair(A):
            pairs = pairs + 1
    print("A gets a pair " + str(100*pairs/total) + "% of the time")


# Simulate total matches and find when B gets a pair
def b_got_pair(total):
    pairs = 0
    for i in range(total):
        deck, _, B = setup()
        B.draw_card(deck)
        if has_pair(B):
            pairs = pairs + 1
    print("B gets a pair " + str(100*pairs/total) + "% of the time")


# Simulate total matches and find when A draws, doesn't get a pair
# then B draws, gets a pair
def b_got_pair_after_a_got_no_pair(total):
    pairs = 0
    for i in range(total):
        deck, A, B = setup()
        A.draw_card(deck)
        if not has_pair(A):
            B.draw_card(deck)
            if has_pair(B):
                pairs = pairs + 1
    print("B gets a pair after A not getting a pair " + str(100*pairs/total) + "% of the time")


def run(times):
    a_got_pair(times)
    b_got_pair(times)
    b_got_pair_after_a_got_no_pair(times)


run(2598960)
