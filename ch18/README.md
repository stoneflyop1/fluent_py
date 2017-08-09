# 使用asyncio执行并发(Concurrency)

> 并发指的是一次处理很多事情。并行指的是一次做很多事情。它们并不同，但是是相关的。一个是关于结构的，一个是关于执行的。并发提供了一个解决可以并行问题的结构化方法。  —— Rob Pike

Python3.3之后的版本可以使用asyncio包。

- 多线程程序与asyncio的比较，给出线程和异步任务(asynchronous tasks)的关系
- asyncio.Future与concurrent.futures.Future的不同
- 异步编程(网络应用中)如何维持高并发而不使用多线程或多进程
- 在异步编程中，协程(conroutine)如何成为一个很重要的改进，与回调函数相比
- 如何通过把阻塞操作转移到线程池来避免事件循环(event loop)阻塞(使用yield from)
- Web应用的高并发实现
- 为什么asyncio对Python生态冲击那么大

## 线程与协程的比较

线程示例代码：[spinner_thread.py](spinner_thread.py)。
asyncio示例代码：[spinner_asyncio.py](spinner_asyncio.py)，使用异步任务。

注：asyncio的示例代码中的协程装饰器不是必须的，但是却是强烈建议的。协程装饰器不具有priming功能。

不同点：

- 异步任务(asyncio.Task)可以比较粗的等价于threading.Thread。“一个任务就像实现了合作多任务的库中的绿色线程，比如：[gevent](http://www.gevent.org/)”
- 任务驱动的是协程，而线程驱动的是可调用对象(callable)
- 你不会自己实例化Task对象，而是通过`asyncio.async(co_ro)`或者`loop.create_task(co_ro)`来生成
- 一个任务生成时，已加入执行队列中；线程需要调用start方法来启动
- 没有API函数可以从外面终止一个线程；而任务有一个cancel方法可以通过触发CancelledError异常取消任务
- supervisor协程必须在主函数的事件循环的trun_until_complete方法中执行

注： yield from与C#中的await类似。在future上使用yield from会自动处理等待完成，而不会阻塞事件循环；因为在asyncio中，yield from被用来把控制权返回给事件循环。asyncio中的future不需要调用result方法来获取结果，如果调用，而调用时还未完成操作，则会触发asyncio.InvalidStateError异常，获取结果应该使用yield from。

关于asyncio中Task和Coroutine的相关详情，参见[官方文档](https://docs.python.org/3/library/asyncio-task.html)。

asyncio的HTTP协议包[aiohttp](https://pypi.python.org/pypi/aiohttp)不在标准库中，需要独立下载安装。