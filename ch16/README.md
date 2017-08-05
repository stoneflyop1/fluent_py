# 协程(coroutines)

- 作为协程操作的生成器的行为和状态
- 使用装饰器(decorator)自动生成(priming)协程
- 使用生成器对象的`close()`和`throw()`方法控制协程
- 协程终止时如何返回值
- 新的`yield from`语法

## 使用生成器构造协程

示例代码见：[priming.py](priming.py)。
注意：每次的yield赋值是要等到下次执行时才会真正赋值。

## 使用装饰器自动Priming

可以通过在装饰器里调用`next()`方法做到自动Priming，示例代码见：[coroaverager.py](coroaverager.py)。

## 协程终止和异常处理

若在send给生成器的数据里触发了异常，则协程会因为未经处理的异常而终止。

通过直接调用生成器上的throw方法可以触发指定异常。

而生成器的close方法调用后，若再send数据到生成器或调用next方法时，则会触发`StopIteration`异常。

示例见：[coerr.py](coerr.py)。

## yield from

`yield from`主要的特性是打开一个双向的通道，从外部调用者到内部的子生成器(subgenerator)，从而值可以被发送或直接从他们进行前后的yield，异常也可以以任何方式抛出，而不需要再协程中添加很多异常处理的样板代码。

PEP380：

- 代理生成器(delegating generator)：`yield from <iterable>`
- 子生成器(subgenerator)：从`yield from <iterable>`得到的`<iterable>`
- 调用者(caller)：调用代理生成器的客户端代码

[python cookbook中的示例代码](https://github.com/dabeaz/python-cookbook/blob/master/src/4/how_to_flatten_a_nested_sequence/example.py)

the meaning of yield from:

- 子生成器yield的任何值都直接传入到代码生成器的调用者
- 使用send方法发送到代理生成器的任何值都直接传入到子生成器。若发送的值为None，则子生成器的next方法被调用；若不是None，则子生成器的send方法被调用；若调用触发了StopIteration异常，子生成器会重启。其他异常都会传播到代理生成器。
- 生成器或子生成器的返回值会触发StopIteration(returnedValue)，在生成器退出时。
- yield from表达式的值是子生成器终止时触发StopIteration异常的第一个参数。
- 抛出到代理生成器的除了GeneratorExit异常会作为子生成器的throw方法参数传入。若调用触发了StopIteration异常，代理生成器会重启；其他异常会传递到代理生成器。
- 若GeneratorExit异常被抛出到代理生成器，或者代理生成器的close方法被调用，则子生成器的close方法将会被调用(如果方法存在的话)。若调用导致了异常，则异常会传递到代理生成器。否则，代理生成器会触发GeneratorExit异常。

## 协程的一个用例：离散事件仿真(Discrete Event Simulation, DES)

