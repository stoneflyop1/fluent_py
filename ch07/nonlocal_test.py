def outer():
    a = 'outer'
    def inner():
        a = 'inner'
        print(a)
    print(a) # outer
    inner() # inner

def nonlocal_outer():
    a = 'outer'
    def inner():
        nonlocal a
        a = 'nonlocal_inner' # change a in the scope of nonlocal_outer
    print(a) # outer
    inner()
    print(a) # nonlocal_inner


if __name__ == "__main__":
    outer() # inner
    nonlocal_outer() # 