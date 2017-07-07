from vector import Vector

v7 = Vector(range(10))
print(v7[-1])
print(repr(v7[1:4]))
print(repr(v7[-1:]))
try:
    v7[1,2]
except TypeError as e:
    print(e)

print(v7.x, v7.y, v7.z, v7.t)

print(format(v7))
print(format(v7, 'h'))