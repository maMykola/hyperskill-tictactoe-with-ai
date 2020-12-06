class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def flatten(self, size):
        return (size - self.y) * size + self.x - 1

    @staticmethod
    def make(inp, bounds):
        data = inp.split(maxsplit=2)
        if len(data) != 2 or not all(x.isnumeric() for x in data):
            raise TypeError

        x, y = (int(x) for x in data)
        if not Coordinate.valid_bounds(x, bounds) or not Coordinate.valid_bounds(y, bounds):
            raise ValueError

        return Coordinate(x, y)

    @staticmethod
    def valid_bounds(number, bounds):
        return bounds[0] <= number <= bounds[1]
