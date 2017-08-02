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

