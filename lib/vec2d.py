class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r})'

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __add__(self, other):
        return Vec2D(self[0] + other[0], self[1] + other[1])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Vec2D(self[0] - other[0], self[1] - other[1])

    def __rsub__(self, other):
        return Vec2D(other[0] - self[0], other[1] - self[1])

    def __len__(self):
        return 2

    def __getitem__(self, key):
        match key:
            case 0:
                return self.x
            case 1:
                return self.y
            case _:
                raise IndexError

    def __setitem__(self, key, newvalue):
        match key:
            case 0:
                self.x = newvalue
            case 1:
                self.y = newvalue
            case _:
                raise IndexError
