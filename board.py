class Board:
    EMPTY_CELL = ' '

    CHIP_X = 'X'
    CHIP_O = 'O'

    def __init__(self, size):
        self.chip = self.CHIP_X
        self.size = size
        self.board = [self.EMPTY_CELL] * size * size
        self.state = False

    def check_state(self):
        self.state = self.check_wins() or self.check_draw()

    def check_wins(self):
        for cells in self.winning_cells():
            if self.is_winning(cells):
                return "{} wins".format(self.board[cells[0]])

    def check_draw(self):
        return "Draw" if self.board.count(self.EMPTY_CELL) == 0 else False

    def winning_cells(self):
        # diagonals
        yield tuple(map(lambda x: x + x * self.size, range(self.size)))
        yield tuple(map(lambda x: (x + 1) * (self.size - 1), range(self.size)))

        for i in range(self.size):
            yield tuple(map(lambda x: i * self.size + x, range(self.size)))  # rows
            yield tuple(map(lambda x: i + x * self.size, range(self.size)))  # cols

    def is_winning(self, cells):
        chips = [self.board[pos] for pos in cells]
        return chips.count(self.CHIP_X) == self.size or chips.count(self.CHIP_O) == self.size

    def can_place(self, coordinate):
        return self.board[coordinate.flatten(self.size)] == self.EMPTY_CELL

    def place_in(self, coordinate):
        self.board[coordinate.flatten(self.size)] = self.chip
        self.turn_chip()

    def place_in_pos(self, pos):
        self.board[pos] = self.chip
        self.turn_chip()

    def turn_chip(self):
        self.chip = self.CHIP_X if self.chip == self.CHIP_O else self.CHIP_O

    def empty_cells(self):
        return tuple(pos for pos, chip in enumerate(self.board) if chip == self.EMPTY_CELL)

    def __str__(self):
        return "---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------".format(*self.board)
