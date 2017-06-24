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