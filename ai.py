from random import choice

from board import Board
from coordinates import Coordinate


class Player:
    def make_move(self, board: Board):
        pass


class User(Player):
    def make_move(self, board: Board):
        while True:
            coordinate = self.take_coordinate(board)
            if board.can_place(coordinate):
                board.place_in(coordinate)
                break
            else:
                print("This cell is occupied! Choose another one!")

    @staticmethod
    def take_coordinate(board: Board):
        while True:
            try:
                return Coordinate.make(input("Enter the coordinates: "), (1, board.size))
            except TypeError:
                print("You should enter numbers!")
            except ValueError:
                print("Coordinates should be from 1 to {}!".format(board.size))


class AI(Player):
    def __init__(self, level="unknown"):
        self.level = level
        self.board = None

    def make_move(self, board: Board):
        print(f'Making move level "{self.level}"')
        self.board = board
        board.place_in_pos(self.take_move())

    def random_move(self):
        return choice(self.board.empty_cells())

    def take_move(self):
        pass


class AIEasy(AI):
    def __init__(self):
        super().__init__(level="easy")

    def take_move(self):
        return self.random_move()


class AIMedium(AI):
    def __init__(self):
        super().__init__(level="medium")

    def take_move(self):
        return self.find_beats() or self.find_beats(opponent=True) or self.random_move()

    def find_beats(self, opponent=False):
        chip = self.board.opponent_chip() if opponent else self.board.chip
        for winning_cells in self.board.winning_cells():
            line = self.board.take_chips(winning_cells)
            if self.can_beat(line, chip):
                return self.find_empty_pos(line)
        return None

    def can_beat(self, line, chip):
        return len(tuple(filter(lambda item: item[1] == chip, line))) == self.board.size - 1

    @staticmethod
    def find_empty_pos(line):
        for pos, cell in line:
            if cell == Board.EMPTY_CELL:
                return pos
        return None


class AIHard(AI):
    def __init__(self):
        super().__init__(level="hard")
