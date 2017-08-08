# 使用Features实现并发(Concurrency)

`concurrent.futures`从Python3.2引入，Python2.5之上的其他版本可以通过[futures包](https://pypi.python.org/pypi/futures/)引入。

所谓的futures，就是可以异步执行的对象。后面要介绍的[asyncio包](../ch18/)也是基于此。

## Futures是什么？

Futures封装了挂起的操作，把放入队列中；我们可以从队列中查询完成的状态，以及操作的结果(或异常)。

以下列出的对象类似：

- concurrent.features.Future
- asyncio.Future
- Twisted中的Deferred
- Tornado中的Future
- JavaScript中的Promise

国旗程序给出了两个实例：一个[同步示例](flags.py)，一个[并发示例](flags_threadpool.py)。其中并发示例我们使用了两种方式，一种是执行器(Executor)直接map(concurrent.futures.ThreadPoolExecutor.map)，所有操作都只能使用同样的参数设置，而且需要按照map顺序获取结果；另一种是先submit加入到执行队列(Schedule)，submit时可以有不同的参数，然后调用as_completed方法获取结果(无固定顺序)。

## 阻塞I/O与全局解释器锁(Global Interpreter Lock, GIL)

- CPython内部并不是线程安全的，它有一个全局解释器锁，使得仅仅允许同时一个线程执行Python的字节码。
- Python代码中没办法摆脱GIL，但是用C写的扩展可以在很耗时的任务中释放GIL，从而可以实现多线程。
- 然而，所有标准库中的执行阻塞I/O的函数都会释放GIL，当等待OS返回结果的时候。

> 每一个阻塞I/O的函数在Python的标准库中都会释放GIL，从而允许其他线程运行。time.sleep方法也会释放GIL。因此，Python线程可以很完美的使用在主要是I/O操作的应用程序中，尽管有GIL。

## 使用concurrent.futures启动进程

[concurrent.futures文档](https://docs.python.org/3/library/concurrent.futures.html)的子标题是“运行平行任务(launching parallel tasks)”。

可以使用`futures.ProcessPoolExecutor`启动多进程，即：启动多个Python实例。ProcessPoolExecutor和ThreadPoolExecutor实现了同一个通用接口`Executor`，因此可以很容易在两者间切换。