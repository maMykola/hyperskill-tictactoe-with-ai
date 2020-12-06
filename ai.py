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

    def make_move(self, board: Board):
        print(f'Making move level "{self.level}"')
        board.place_in_pos(self.take_move(board))

    def take_move(self, board: Board):
        pass


class AIEasy(AI):
    def __init__(self):
        super().__init__(level="easy")

    def take_move(self, board: Board):
        empty_cells = board.empty_cells()
        return choice(empty_cells)


class AIMedium(AI):
    def __init__(self):
        super().__init__(level="medium")


class AIHard(AI):
    def __init__(self):
        super().__init__(level="hard")

