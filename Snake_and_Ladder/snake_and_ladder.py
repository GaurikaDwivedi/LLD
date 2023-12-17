import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.moves = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, spaces):
        self.position += spaces
        self.moves += 1

class Board:
    def __init__(self, size):
        self.size = size
        self.player_positions = []
        self.snake_positions = []
        self.ladder_positions = []

    def move_player(self, player, roll):
        new_pos = player.position + roll
        if new_pos > self.size:
            return

        for i in range(0, len(self.ladder_positions), 2):
            if new_pos == self.ladder_positions[i]:
                new_pos = self.ladder_positions[i + 1]
                break

        for i in range(0, len(self.snake_positions), 2):
            if new_pos == self.snake_positions[i]:
                new_pos = self.snake_positions[i + 1]
                break

        player.position = new_pos

    def check_winner(self, player):
        if player.position == self.size:
            print(player.name + " wins!")
            return True
        return False

class Game:
    def __init__(self, board_size, player_names, snakes, ladders):
        self.board = Board(board_size)
        self.players = [Player(name) for name in player_names]
        self.snakes = snakes
        self.ladders = ladders
        self.initialize_board()

    def initialize_board(self):
        for snake in self.snakes:
            self.board.snake_positions.extend(snake)

        for ladder in self.ladders:
            self.board.ladder_positions.extend(ladder)

    def play(self):
        while True:
            for player in self.players:
                roll = player.roll_dice()
                print(player.name + " rolled a " + str(roll))
                self.board.move_player(player, roll)
                print(player.name + " is now on square " + str(player.position))
                if self.board.check_winner(player):
                    return

if __name__ == "__main__":
    player_names = ["Player 1", "Player 2"]
    snakes = [(17, 7), (54, 34)]
    ladders = [(62, 81), (87, 96)]
    game = Game(100, player_names, snakes, ladders)
    game.play()
