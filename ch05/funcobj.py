##############################
# function as object
def factorial(n):
    ''' return n! '''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(10)) # call function
print(factorial.__doc__) # call prop of function
print(type(factorial)) # get type as an object

fact = factorial # assign function to a variable
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(fact, range(11))))

#######################
# Higher Order Functions
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len)) # key为函数参数
def reverse(word):
    return word[::-1]
print(reverse('testing'))
print(sorted(fruits, key=reverse))

from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

print('all([]) ==', all([]))
print('any([]) ==', any([]))

print([(obj, callable(obj)) for obj in (abs, str, 13)])