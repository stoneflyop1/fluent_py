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

示例代码见：[clockdeco.py](clockdeco.py)。注意：`@functools.wraps(func)`的使用。

## 标准库中的装饰器

### functools.lru_cache

最近使用缓存(LRU)，一个常见场景是使用在需要重复计算函数值的递归函数中。示例见：[fibo_cache.py](fibo_cache.py)。标准库函数原型如下：

```python
functools.lru_cache(maxsize=128, typed=False)
```

注意：所有使用此装饰器的函数参数都需要是可哈希的。

### functools.singledispatch

使用singledispatch可以实现类似其他语言的泛型特性，见示例代码：[singledispatch.py](singledispatch.py)。

## 函数使用多装饰器修饰(Stacked Decorators)

```python
@d1
@d2
def f(): print('f')
# Same as above
def f(): print('f')
f = d1(d2(f))
```

## 参数化的装饰器(Parameterized Decorators)

装饰器函数再次返回一个装饰器，这样就可以通过装饰器函数的参数传入一些设置或条件。
示例参见：[clockdeco.py](clockdeco.py)中的`clock_param`。