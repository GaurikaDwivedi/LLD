import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class BlackjackCard(Card):
    def __init__(self, suit, value):
        super().__init__(suit, value)

    def get_value(self):
        return 10 if self.value >= 10 else self.value

class Deck:
    def __init__(self):
        self.cards = [BlackjackCard(s, v) for s in range(4) for v in range(1, 12)]

    def shuffle(self):
        random.shuffle(self.cards)

class Shoe:
    def __init__(self, n):
        self.decks = [Deck() for _ in range(n)]

    def shuffle(self):
        for deck in self.decks:
            deck.shuffle()

class Hand:
    def __init__(self):
        self.cards = []

    def get_hard_value(self):
        return sum(card.get_value() for card in self.cards)

    def get_soft_value(self):
        total_value = sum(card.get_value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.get_value() == 11)

        while total_value > 21 and aces > 0:
            total_value -= 10
            aces -= 1

        return total_value

class Player:
    def __init__(self):
        self.stake = 0
        self.hand = Hand()

class Game:
    def __init__(self, n):
        self.shoe = Shoe(n)
        self.players = []

    def run(self):
        self.shoe.shuffle()

        for player in self.players:
            player.stake = 100
            player.hand = Hand()

        for _ in range(2):
            for player in self.players:
                player.hand.cards.append(self.shoe.decks[0].cards.pop())

        for i, player in enumerate(self.players, 1):
            print(f"Player {i}: {player.hand.get_hard_value()}")

        for player in self.players:
            while player.hand.get_soft_value() < 17:
                player.hand.cards.append(self.shoe.decks[0].cards.pop())
                print(f"Player {self.players.index(player) + 1}: {player.hand.get_hard_value()}")

        max_value = 0
        for player in self.players:
            if 21 >= player.hand.get_soft_value() > max_value:
                max_value = player.hand.get_soft_value()

        for player in self.players:
            if player.hand.get_soft_value() == max_value:
                print(f"Player {self.players.index(player) + 1} wins")

if __name__ == "__main__":
    game = Game(1)
    game.players.append(Player())
    game.players.append(Player())
    game.run()
