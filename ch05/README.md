# 函数作为第一类对象(First-Class Functions)

## 把函数作为对象使用

函数定义后，可以作为对象使用，比如：可以给其他变量赋值为一个函数，可以访问函数的文档属性`__doc__`等。

## 高阶函数(Higher-Order Functions)

高阶函数具有如下特性之一：

- 以函数作为参数
- 以函数作为返回值

示例有：`sorted`, `map`, `filter`, `reduce`等。

注： python3中map和filter返回的是生成器(generator)，迭代器的一种形式，而python2中它们返回的是列表(list)。

python3中reduce被转移到了functools模块中(python2中是内置函数)

```python
from functools import reduce
val = reduce(operator, sequence)
```

另外两个常用的与reduce类似函数为：

- all(iterable) => iterable中所有元素为真时，返回True，否则False；`all([]) == True`
- any(iterable) => iterable中任意一个元素为真时，返回True，否则False；`any([]) == False`


## 匿名函数(Anonymous Functions)

使用lambda关键字可以创建一个匿名函数

```python
f = lambda n: n
print(f(1))
```

## 可调用对象(Callable Objects)

可以使用内置的`callable`函数判断是否对象是可调用的。

- 用户自定义函数(User-defined functions)：使用def或lambda关键字创建的函数
- 内置函数
- 内置方法，如：dict.get
- 方法，即：类中定义的函数
- 类：当调用时，类会调用它的`__new__`方法创建类的实例，然后调用`__init__`方法初始化实例对象
- 类实例：若一个类中定义了`__call__`方法，则它可以像一个函数那样被调用
- [生成器函数(Generator functions)](../ch14/)：使用`yield`关键字的函数或方法

## 自定义可调用类型

只需对象实现`__call__`实例方法，实例代码见：[call.py](call.py)。

