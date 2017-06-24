from clockdeco import clock0

@clock0
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-2) + fibonacci(n-1)

import functools

@functools.lru_cache()
@clock0
def fibo_cache(n):
    if n < 2: return n
    return fibo_cache(n-2) + fibo_cache(n-1)

if __name__ == '__main__':
    print(fibonacci(6))
    print(fibo_cache(6))