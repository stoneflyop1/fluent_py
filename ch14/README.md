# 迭代器、生成器(Iterables, Iterators, and Generators)

> 每个生成器都是迭代器：生成器完全实现了迭代器接口。

python3中的range函数返回的也是一个类生成器对象，而不是一个完整的list。若要生成一个list，可以：list(range(100))。

python中的集合都是可遍历的(iterable)，内部都由迭代器支持：

- for循环
- 集合类型的构造和扩展
- 从文本文件中读取行
- 列表(list)、词典(dict)以及集合(set)推导(comprehensions)
- 元组拆包(tuple unpacking)
- 函数调用时的*参数的实际参数拆包

本章主题：

- `iter(...)`函数如何zxai 内部处理可遍历对象
- python中如何实现经典的迭代器设计模式
- 详细介绍生成器函数如何工作
- 经典的迭代器如何通过生成器函数或生成器表达式代替
- 使用标准库中的一般意义的生成器函数
- 使用`yield from`组合生成器
- 一个案例：使用生成器函数处理数据库中的大的数据集
- 为什么生成器和协同程序(coroutine)是不同的，且不要搞混？

## 可遍历性

iter(x)调用时会先找`__iter__`方法，若未找到，则会找`__getitem__`方法(需要接受一个从0开始的整型参数)；而对象若未实现`__iter__`方法，对象就不是abc.Iterable的子类。因此， 判断一个对象是否可遍历的只需要调用iter方法并捕获TypeError即可(无法遍历的对象会抛出TypeError异常)。

可遍历对象有一个可供调用的方法：`__iter__`。

迭代器由可遍历对象生成，有两个内置方法：

- `__next__`：返回下一个可用的值，若已到最后一个，则抛出StopIteration异常
- `__iter__`：返回自己

使用不同方式进行迭代的示例代码见：

- [getitem方式](sentence.py])
- [经典迭代器模式](sentence_iter.py])
- [使用生成器](sentence_gen.py])
- [使用生成器,lazy](sentence_gen2.py])
- [等差数列示例(Arithmetic Progression)](ap.py)

注：itertools模块跟.NET中的LINQ类似。