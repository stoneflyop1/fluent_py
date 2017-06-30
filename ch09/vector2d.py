from array import array
import math

class Vector2d:
    typecode = 'd' # class attribute used to convert Vector2d to/from bytes
    __slots__ = ('__x', '__y')
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self): # readonly
        return self.__x

    @property
    def y(self): # readonly
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self): # now you can use unpacking like x,y = Vector2d(3,4)
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

if __name__ == '__main__':
    v1 = Vector2d(3,4)
    print(v1.x, v1.y)
    x,y = v1
    print(x,y)
    print(repr(v1))
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    print(abs(v1))
    print((bool(v1), bool(Vector2d(0,0))))

    octets = bytes(v1)
    v2 = Vector2d.frombytes(octets)
    print(v2)
    try:
        print(v2.__dict__)
    except AttributeError as e: # raise attribute error when using __slots__
        print(e)
    print(octets)
    print(len(octets))
    try:
        v1.typecode = 'f' # raise attribute error when using __slots__
        o1 = bytes(v1)
        print(o1)
        print(len(o1))
    except AttributeError as e:
        print(e)