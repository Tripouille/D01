import traceback
from numbers import Number


class Vector:
    def __init__(self, arg):
        if (isinstance(arg, list)
                and all(map(lambda x: isinstance(x, float), arg))):
            self.values = arg
        elif isinstance(arg, int):
            self.values = [float(x) for x in range(arg)]
        elif isinstance(arg, range):
            self.values = [float(x) for x in arg]
        elif (isinstance(arg, tuple) and len(arg) == 2
                and isinstance(arg[0], int) and isinstance(arg[1], int)):
            self.values = [float(x) for x in range(arg[0], arg[1])]
        else:
            raise TypeError("must be list, int, range, or tuple")
        self.size = len(self.values)

    def __str__(self):
        return ("(Vector {})".format(self.values))

    def __repr__(self):
        return ("(Vector {})".format(self.values))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector operand + only accept vector")
        if self.size != other.size:
            raise ValueError("Vector must have the same size.")
        total = []
        for i in range(self.size):
            total.append(self.values[i] + other.values[i])
        return (Vector(total))

    def __radd__(self, other):
        return (self + other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector operand - only accept vector")
        if self.size != other.size:
            raise ValueError("Vector must have the same size.")
        total = []
        for i in range(self.size):
            total.append(self.values[i] - other.values[i])
        return (Vector(total))

    def __rsub__(self, other):
        return (self - other)

    def __truediv__(self, other):
        if not isinstance(other, Number):
            raise TypeError("Vector operand / only accepts numbers")
        return (Vector([v / other for v in self.values]))

    def __rtruediv__(self, other):
        raise TypeError("Vector can't be used as divisor")

    def __mul__(self, other):
        if isinstance(other, Number):
            return (Vector([v * other for v in self.values]))
        elif isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError("Vector must have the same size.")
            return sum(self.values[i] * other.values[i]
                       for i in range(self.size))
        else:
            raise TypeError("Vector operand * only accepts numbers or vector")

    def __rmul__(self, other):
        return (self * other)


print("test des constructeur:")
print(Vector([0.0, 0.1, 0.4]))
print(Vector(3))
print(Vector((7, 30)))
print(Vector(range(5, 10)))
try:
    print(Vector("*PROUT*"))
except Exception:
    traceback.print_exc()
print("test des calculs:")
v1 = Vector((0, 5))
v2 = Vector(5)
print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v1 =", v1)
print("v1 / 2 =", v1 / 2)
print("v1 * 3 =", v1 * 3)
print("v1 * 2 =", v1 * v2)