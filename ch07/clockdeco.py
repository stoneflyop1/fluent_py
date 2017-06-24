import time

def clock(func):
    ''' cannot use keyword arguments '''
    def clocked(*args):
        t0 = time.perf_counter() # 记录开始时间
        result = func(*args) # 调用原始函数
        elapsed = time.perf_counter() - t0 # 记录原始函数调用时间
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result # 返回原始函数的返回值
        
    return clocked

import functools

def clock0(func):
    ''' deal with \* and \** arguments '''
    @functools.wraps(func) # 用来处理关键字变量参数
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked