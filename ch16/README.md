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