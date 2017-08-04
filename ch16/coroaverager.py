def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

from coroutil import coroutine

@coroutine
def averager_auto():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager_value():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None: break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg) # priming it by calling next
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))

    
    averager = coroutine(averager)
    coro_avg1 = averager()
    print('Decorator...')
    print(coro_avg1.send(10))
    coro_avg2 = averager_auto()
    print('auto Decorator...')
    print(coro_avg2.send(20))

    coro_av = averager_value()
    next(coro_av)
    coro_av.send(10) # no print
    coro_av.send(30)
    coro_av.send(6.5)
    try:
        coro_av.send(None)
    except StopIteration as exc:
        print(exc.value)