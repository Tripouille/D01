import sys
sys.path.append('../ex02/')  # noqa: E402
from vector import Vector
from matrix import Matrix


m = Matrix([[1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]], (3, 2))
m2 = Matrix((3, 2))
m3 = Matrix([[10.0, 20.0, 0.0],
            [30.0, 40.0, 0.0]], (2, 3))
print("m", m)
print("m2", m2)
mv = Matrix([[1.0], [2.0]])
v = Vector([-5.0, 7.0])
print("TEST +")
print("m + m2", m + m2)
print("m + m", m + m)
print("mv", mv)
print("v", v)
print("mv + v", mv + v)
print("v + mv", v + mv)
print("TEST -")
print("m - m2", m - m2)
print("m - m", m - m)
print("mv", mv)
print("v", v)
print("mv -  v", mv - v)
print("TEST /")
print("m", m)
print("m / -4", m / -4)
print("TEST *")
print("m", m)
print("m * -2", m * -2)
print("m", m)
print("m3", m3)
print("m * m3", m * m3)
print("m", m)
print("v", v)
print("m * v", m * v)
ve1 = Vector([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
ma1 = Matrix([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
print("ve1", ve1)
print("ma1", ma1)
print("ve1 * ma1", ve1 * ma1)
print("ma * ve1", ma1 * ve1)
