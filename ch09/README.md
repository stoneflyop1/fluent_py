# python对象

- 使用内置函数自定义对象表示(如：repr(), bytes()等)
- 实现一个可选的构造器作为类方法
- 扩展对象的字符串格式化(str.format)
- 提供对象的只读属性
- 对象的哈希
- 使用`__slots__`节省内存

## 对象表示(Object Representations)

代码示例见：[vector2d.py](vector2d.py)

- `__repr__` -> `repr()` => 开发者友好的字符串表示
- `__str__`  -> `str()`  => 用户友好的字符串表示
- `__bytes__` => 字符序列表示
- `__format__` -> `format()` or `str.format()` => 格式化字符串

## 一个可选的构造函数

- 类方法(`classmethod`)：第一个参数为类的类型(一般命名为：`cls`)，比如：Vector2d。
- 静态方法(`staticmethod`)：没有占位参数，使用场景不多，一般可以用函数代替

代码示例见：[methoddemo.py](methoddemo.py)

## 格式化显示(Formatted Displays)

`format()`以及`str.format()`用来格式化显示对象，底层调用的是对象的`__format__(format_spec)`方法。format_spec有如下两种情况：

- 作为内置函数`format`的第二个参数
- 具有冒号(:)分隔的由{}限定的格式使用`str.format`方法：冒号左侧的为`替换字段语法(replacement field syntax)`；右侧的为[format_spec](https://docs.python.org/3/library/string.html#formatspec)

```python
>>> brl = 1/2.45  # BRL to USD 汇率
>>> brl
0.4081632653061224
>>> format(brl, '0.4f')  # format_spec = '0.4f'
'0.4082'
>>> '1 BRL = {rate:0.2f} USD'.format(rate=brl)  # str.format
'1 BRL = 0.41 USD”
>>> format(45,'b')
'101101'
>>> format(2/3, '.1%')
'66.7%'
```

## 可哈希

为了在集合中使用Vector2d，我们需要实现`__hash__`方法，否则会报`TypeError`。

```python
>>> v1 = Vector2d(3,4)
>>> set([v1])
Traceback (most recent call last):
  File "vector2d.py", line 71, in <module>
    print(set([v1]))
TypeError: unhashable type: 'Vector2d'
```

## 私有的(private)、以及受保护的(protected)字段(Attribute)

一般地，以双下划线开始，而不以双下划线结束的变量作为私有字段(此方式的字段会写入对象的`__dict__`属性词典中)；而以单下划线开始的变量作为受保护的共享字段。不过这只是大部分python程序的约定，并不是强制性的。

## 使用类的`__slots__`特性节省内存

`__slots__`是一个元组，指定说类的实例仅仅包含这些属性(attribute)，而类的实例中也将不再存在`__dict__`属性(因为只会保留slots中的类似`__attr__`属性)，从而对于大量对象的处理可以节省大量内存。

注意：如果使用了`__slots__`以及`__weakref__`，`__weakref__`也要包含到`__slots__`元组中。

### slots的问题

- 若使用了slots，则所有的子类都需要定义slots
- 只有slots中给出`__dict__`，才能包含所有其他定义的类似属性，但这样就无法节省内存了
- 若slots中没有包含`__weakref__`，则没法启用对象的弱引用功能
