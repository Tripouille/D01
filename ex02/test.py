import traceback
from vector import Vector


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
