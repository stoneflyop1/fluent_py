from coroaverager import averager_auto

coro_avg = averager_auto()
print(coro_avg.send(40))
print(coro_avg.send(50))
try:
    coro_avg.send('spam')
except TypeError as e:
    print(e)
try:
    coro_avg.send(60)
except StopIteration:
    print('StopIteration')

coro_avg2 = averager_auto()
print(coro_avg2.send(70))
coro_avg2.close()
# next(coro_avg2)
# coro_avg2.send(80)


class DemoException(Exception):
    ''' for demo '''

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


from inspect import getgeneratorstate
print('*'*20+'close')
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.close()
print(getgeneratorstate(exc_coro))
try:
    exc_coro.send(222)
    #next(exc_coro)
except Exception as e:
    print(repr(e))
print('*'*20+'throw will catch DemoException')
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(22)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))
print('*'*20+'throw will not catch other exception')
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(33)
try:
    exc_coro.throw(ZeroDivisionError)
except Exception as e:
    print(repr(e))
print(getgeneratorstate(exc_coro))