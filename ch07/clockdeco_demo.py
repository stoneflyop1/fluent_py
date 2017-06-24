import time
from clockdeco import clock, clock_param

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

@clock_param()
def snooze_param(seconds):
    time.sleep(seconds)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))
    print(factorial.__name__)
    for i in range(3): snooze_param(.123)