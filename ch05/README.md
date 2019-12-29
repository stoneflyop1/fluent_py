# 函数作为第一类对象(First-Class Functions)

## 把函数作为对象使用

函数定义后，可以作为对象使用，比如：可以给其他变量赋值为一个函数，可以访问函数的文档属性`__doc__`等。

## 高阶函数(Higher-Order Functions)

高阶函数具有如下特性之一：

- 以函数作为参数
- 以函数作为返回值

示例有：`sorted`, `map`, `filter`, `reduce`等。

注： python3中map和filter返回的是生成器(generator)，迭代器的一种形式，而python2中它们返回的是列表(list)。

python3中reduce不再作为内置函数，转移到了functools模块中

```python
from functools import reduce
val = reduce(operator, sequence)
```

另外两个常用的与reduce类似函数为：

- all(iterable) => iterable中所有元素为真时，返回True，否则False；`all([]) == True`
- any(iterable) => iterable中任意一个元素为真时，返回True，否则False；`any([]) == False`
- sum(iterable) => 对迭代器元素进行求和


## 匿名函数(Anonymous Functions)

使用lambda关键字可以创建一个匿名函数，其本质就是一个函数，会创建一个函数对象。

```python
f = lambda n: n
print(f(1))
```

## 可调用对象(Callable Objects)

可以使用内置的`callable`函数判断是否对象是可调用的。

- 用户自定义函数(User-defined functions)：使用def或lambda关键字创建的函数
- 内置函数，如：len
- 内置方法，如：dict.get
- 方法，即：类中定义的函数
- 类：当调用时，类会调用它的`__new__`方法创建类的实例，然后调用`__init__`方法初始化实例对象
- 类实例：若一个类中定义了`__call__`方法，则它可以像一个函数那样被调用
- [生成器函数(Generator functions)](../ch14/)：使用`yield`关键字的函数或方法

## 自定义可调用类型

只需对象实现`__call__`实例方法，实例代码见：[call.py](call.py)。

```python
class TestCall:
    ''' a callable demo '''
    def __init__(self):
        pass
    def __call__(self):
        return 'called by call'

tc = TestCall()
print(tc()) # 'called by call'
print(callable(tc)) # True
```

## 函数内省(Function Introspection)

可以用`__dir__`函数显示函数上定义的Attributes。

| 名称 | 类型 | 描述 |
| ---- | ---- | ---- |
| `__annotations__` | dict | 参数和返回值标记 |
| `__call__` | method_wrapper | 实现可调用对象协议(callable object protocol) |
| `__closure__` | tuple | 函数闭包，也就是自由变量绑定 |
| `__code__` | code | 编译为字节码(bytecode)的函数元数据(metadata)以及函数体(body) |
| `__defaults__` | tuple | 参数的默认值 |
| `__kwdefaults__` | dict | 关键字参数的默认值词典 |
| `__name__` | str | 函数名 |
| `__qualname__` | str | [函数全称](https://www.python.org/dev/peps/pep-3155/)，如：Random.choice |



## 函数参数从位置参数到关键字参数

python3提供了仅作为关键字参数的函数参数，方法是放在一个星号参数之后。
示例见：[keyparam.py](keyparam.py)

```python
def tag(name, *content, cls=None, **attrs):
    ''' generate one or more HTML tags 

    @param {name} 位置参数，也可以按照关键字参数传入

    @param {cls} 仅能作为关键字参数(因为在星号参数之后给出)，即：传入参数时必须写cls=value；是python3的特性

    @param {content} 所有从第二个开始不是以关键字传入的参数都会以tuple的形式被此参数捕获

    @param {attrs} 按照词典展开参数，若可以匹配位置参数则会认为是位置参数，其他作为key-value形式提供给函数
    '''
    pass
tag('p', 'hello', 'world') # hello world as content
tag('p', 'hello', id=33) # id is keyword param in attrs
tag('p', 'hello', 'world', cls='sidebar') # hello world as content
tag(content='testing', name='img') # name passed as keyword param
my_tag = {'name':'img', 'title':'Sunset boulevard',
     'src':'sunset.jpg', 'cls':'framed'}
tag(**my_tag) # get named param from dict, then others as attrs param
```

## 函数标记(Function Annotations)

python3可以通过标记指定参数、返回值的类型和条件等，相当于附加给函数的元数据。

注意：若使用函数时，参数会返回值与标记不符，python解释器不会做任何事情；只不过一些IDE、框架、装饰器等可以根据函数标记处理一些事情。

示例见：[funcanno.py](funcanno.py)

## 函数式编程

待看
