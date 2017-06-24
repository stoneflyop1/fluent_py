a = [1,2,3]
b = a
a.append(4)
print(a is b) # True

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
y = Gizmo()
print(x is y) # False
try:
    z = Gizmo() * 10
except TypeError as e:
    print(e)