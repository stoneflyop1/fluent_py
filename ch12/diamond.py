class A:
    def ping(self): print('A ping:', self)

class B(A):
    def pong(self): print('B pong:', self)

class C(A):
    def pong(self): print('C PONG:', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

if __name__ == '__main__':
    d = D()
    d.pong()
    C.pong(d)
    print(D.__mro__)
    print_mro(D)
    d.pingpong()