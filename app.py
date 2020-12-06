from ai import Player
from board import Board


class Game:
    def __init__(self, player1: Player, player2: Player, size: int = 3):
        self.board = Board(size)
        self.player1 = player1
        self.player2 = player2

    def run(self):
        for player in self.get_players():
            print(self.board)

            player.make_move(self.board)
            self.board.check_state()

            if self.board.state:
                print(self.board.state)
                break

    def get_players(self):
        while True:
            yield self.player1
            yield self.player2
