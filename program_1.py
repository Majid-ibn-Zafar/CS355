from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(10):
            for j in range(i+1):
                self.cards.append(i+1)
        shuffle(self.cards)

    def get_card(self):
        return self.cards.pop(0)


class Player:
    def __init__(self):
        self.hand = []

    def give_card(self, card):
        self.hand.append(card)

    def draw_card(self, deck):
        self.hand.append(deck.get_card())

    def has_pair(self):
        seen = set()
        for card in self.hand:
            if card in seen:
                return True
            seen.add(card)
        return False


a_win_count = 0
b_win_count = 0
number_of_rounds = 0

print("Simulating 10000 games...")
for _ in range(10000):
    deck = Deck()
    player_a = Player()
    player_b = Player()

    card_a = deck.get_card()
    card_b = deck.get_card()

    player_a.give_card(min(card_a, card_b))
    player_b.give_card(max(card_a, card_b))

    current_player = player_a
    rounds_played = 0
    while True:
        if current_player is player_a:
            rounds_played += 1

        current_player.draw_card(deck)
        if current_player.has_pair():
            if current_player is player_a:
                a_win_count += 1
            else:
                b_win_count += 1
            number_of_rounds += rounds_played
            break

        if current_player is player_a:
            current_player = player_b
        else:
            current_player = player_a

print("Player A won " + str(a_win_count/100) + "% of games")
print("Player B won " + str(b_win_count/100) + "% of games")
print("On average, a game lasted " + str(number_of_rounds/10000) + " rounds")
