import random

class BingoCage:
    ''' a callable demo '''

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))
print(dir(bingo.pick))
print(bingo.pick.__annotations__)


class TestCall:
    ''' a callable demo '''
    def __init__(self):
        pass
    def __call__(self):
        return 'called by call'

tc = TestCall()
print(tc())
print(callable(tc)) # True