# 函数装饰器(Decorators)和闭包(Closures)

装饰器为接受函数作为参数，并且以函数作为输出的函数。

- 装饰器具有用不同的函数替换装饰器函数的能力
- 装饰器在模块加载时会立即执行

```python
@decorate
def target():
    print('running target()')
# Same with below
def target():
    print('runing target()')
target = decorate(target)
```

## 变量的作用域规则(Variable Scope Rules)


- 函数内部使用全局变量
    ```python
    def f1(a):
        print(a)
        print(b) # b is not defined in local, so it supposed to be in global
    try:
        print(f1(3))
    except NameError as e:
        print('b is not defined in global yet: ' + str(e))
    b = 6
    print(f1(3))
    ```
- 函数内部对全局变量赋值
    ```python
    b = 6
    def f2(a):
        print(a)
        print(b) # here b is local because of below assignment
        b = 9
    def f3(a):
        global b
        print(a)
        print(b) # b is global now
        b = 9 # change global b
    try:
        f2(3)
    except UnboundLocalError as e:
        print('b is local now: ' + str(e))
    f3(3)
    ```

## 闭包(Closures)

函数中定义函数，在内层函数捕获外层函数中定义的变量，外层函数返回内层函数定义。

```python
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def make_suffient_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1 # count must be nonlocal because it is being assigned value
        total += new_value # total must be nonlocal because it is being assigned value
        return total / count

    return averager
```

## 实现一个简单的装饰器