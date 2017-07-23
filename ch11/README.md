# 接口：从协议(Protocol)到抽象基础类(Abstract Base Class, ABC)

从python2.6开始引入了ABC。

## Python文化中的接口和协议

```python
class SizedClass:
    def __len__(self): return 0
from collections import abc
print(isinstance(SizedClass(), abc.Sized)) # True
```

建议只使用`isinstance`或者`issubclass`方法判断一个实例或类是否实现了ABC中的接口。有一个例外，某些Python API接受一个简单的字符串(str)或者一个字符串序列；在str情况下，为了方便处理，一般我们会包装一个列表；但是因为str是序列类型，此时为了跟其他序列区分，可以用`isinstance(x,str)`方法做检查。

> ABC用来封装非常一般化的概念、抽象，由框架引入，如：“序列”，“数字”等。我们一般不需要创建新的ABC类，仅仅正确使用现有的，就可以获得99.9%的益处，且不会导致严重的设计失误。

注：ABC中的类有些是抽象方法，可以认为是抽象类。当实现其中的抽象类时，若未实现其中的某些抽象方法，则在import时并不会报错，而是在使用那些方法时会报`TypeError`。

## 标准库中的ABC

- collections.abc (Lib/_collections_abc.py)
  - Iterable  --> `__iter__`
  - Container --> `__contains__`, in operator
  - Sized     --> `__len__`, len()
  - Sequence <-- (Iterable, Container, Sized)
  - Mapping  <-- (Iterable, Container, Sized)
  - Set      <-- (Iterable, Container, Sized)
  - Iterator <-- (Iterable)
- numbers isinstance (Number, Complex, Real, Rational, Integral)
- [abc.ABC (Lib/abc.py)](https://docs.python.org/3/library/abc.html)