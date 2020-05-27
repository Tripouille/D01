import sys
sys.path.append('../ex02/')  # noqa: E402
from vector import Vector
from numbers import Number


class Matrix:
    def __init__(self, data, shape=None):
        if isinstance(data, list):
            if not all([isinstance(d, list) for d in data]):
                raise ValueError("data list must contain only list")
            if not all([len(d) == len(data[0]) for d in data]):
                raise ValueError("only support rectangular shape.")
            for row in data:
                if not all([isinstance(n, float) for n in row]):
                    raise ValueError("list must contain only float")
            self.data = data
        elif isinstance(data, tuple):
            if not len(data) == 2:
                raise ValueError("tuple size must be 2 (m, n)")
            if not all([isinstance(v, int) for v in data]):
                raise ValueError("tuple must contain only int")
            if not all([v > 0 for v in data]):
                raise ValueError("tuple must contain only value > 0")
            self.data = [[0.0 for c in range(data[1])] for r in range(data[0])]
        else:
            raise TypeError("unsupported data type.")
        if shape is not None and shape != (len(self.data), len(self.data[0])):
            raise ValueError("invalid shape: {} should be {}."
                             .format(shape, (len(self.data),
                                             len(self.data[0]))))
        self.shape = (len(self.data), len(self.data[0]))

    def __str__(self):
        res = "(Matrix\n" + '\n'.join(' '.join(str(line))
                                      for line in self.data)
        return (res + ")")

    def __repr__(self):
        res = "(Matrix " + '\n'.join(' '.join(str(line)) for line in self.data)
        return (res + ")")

    def __add__(self, other):
        if isinstance(other, Vector) and self.shape[1] == 1:
            return (self + Matrix([[v] for v in other.values]))
        elif isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("values must have the same shape")
            return (Matrix([[*map(lambda x, y: x + y,
                            self.data[i], other.data[i])]
                            for i in range(self.shape[0])]))
        else:
            return NotImplemented

    def __radd__(self, other):
        return (self + other)

    def __sub__(self, other):
        if isinstance(other, Vector) and self.shape[1] == 1:
            return (self - Matrix([[v] for v in other.values]))
        elif isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("values must have the same shape")
            return (Matrix([[*map(lambda x, y: x - y,
                            self.data[i], other.data[i])]
                            for i in range(self.shape[0])]))
        else:
            return NotImplemented

    def __rsub__(self, other):
        return (self - other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return (Matrix([[*map(lambda x: x / other,
                    self.data[i])] for i in range(self.shape[0])]))
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return (Matrix([[*map(lambda x: x * other,
                    self.data[i])] for i in range(self.shape[0])]))
        elif isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("self collumn must be = to the other line.")
            m = []
            for r in range(self.shape[0]):
                row = []
                for c in range(other.shape[1]):
                    row.append(sum([self.data[r][i] * other.data[i][c]
                                    for i in range(self.shape[1])]))
                m.append(row)
            return Matrix(m)
        elif isinstance(other, Vector):
            if self.shape[1] != other.size:
                raise ValueError("self collumn must be = to the vector line.")
            v = []
            for r in range(self.shape[0]):
                v.append(sum([self.data[r][i] * other.values[i]
                         for i in range(self.shape[1])]))
            return Vector(v)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Number):
            return (self * other)
        if isinstance(other, Vector):
            if self.shape[0] != 1:
                raise ValueError("self line must be one.")
            m = []
            for li in range(other.size):
                m.append([other.values[li] * self.data[0][c]
                          for c in range(self.shape[1])])
            return Matrix(m)
        return NotImplemented
