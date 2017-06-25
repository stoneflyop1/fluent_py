## 对象引用、可变性以及回收(Object References, Mutability, and Recycling)

> 每个对象都有一个标识(identity)、类型(type)以及值(value)。对象标识在对象创建后从不变化；你可以把它当做对象在内存中的地址。`is`操作符用来比较对象的标识；函数`id(obj)`返回标识的整型值。

## 变量不是用来装对象的盒子(Variables Are Not Boxes)

变量并不会保存对象，而只是对象的一个标签(label)， 代码示例见：[objectlabel.py](objectlabel.py)。

## 标识、相等和别名(Identity, Equality, and Aliases)

代码示例见：[equality.py](equality.py)

### 选择==还是is

- `==`用来比较对象的值
- `is`用来比较对象的标识
- `is`操作符比`==`执行速度更快，因为它无法被重载；而`==`其实是对象方法`__eq__`的语法糖
- 与`None`进行比较请使用`is`或`is not`

### 元组(Tuples)的相对不可变性(Immutability)

元组跟其他的集合类型(list, dict, set等)一样，保存的是对象的引用。若引用的对象是可变的，引用对象就可以变化，即使元组本身没有变化。

## 对象拷贝默认是浅拷贝(shallow copy)

对象拷贝默认为浅拷贝，因此对于可变类型对象，拷贝的只是引用，而不是引用的内容。

代码示例见：[objectcopy.py](objectcopy.py)

若需要深拷贝，可以使用`copy`模块中的`deepcopy`方法，即使有循环引用也可以处理。

## 函数参数为引用(Function Parameters as References)

变量作为函数参数传入多个函数时，变量在这些函数中是共享的，函数调用中无法改变此变量的标识(Identity)，但是作为可变类型，是可以改变引用的值的。

示例代码见：[paramref.py](paramref.py)

- 可变类型作为函数参数的默认值是一个坏主意(因为此参数可能会在多个函数中共享实例，即使是`默认的空列表也会共享，而在函数内部使用空列表不会有此问题，貌似是因为函数参数若使用空列表，使用的是同一个[]，而若在函数内部赋值给[]，则每次实例化都会针对[]生成不同的id`)
- 可变参数的防范编程，考虑可变类型参数在函数内部的修改是否需要影响外部的变量


注：空列表作为函数参数的问题，关键在于python解释器如何生成空列表，在某些情况下可能会重用空列表的引用，某些情况下可能会新建空列表；若要确保新建空列表，可以使用`list([])`。

## 垃圾回收(Garbage Collection)和删除(del)

> 对象从来不会显示地被销毁，当他们无法触及的时候，会被垃圾回收。

del语句只是删除名字(用来引用对象的名字)，而不是对象本身。真正删除对象的是垃圾回收。

- del名字的对象是最后一次引用
- del名字的对象已无法触及
- 重新绑定名字到其他对象若使得以前的对象引用个数达到了0，也会导致被回收

CPython中使用的是引用计数方式进行垃圾回收。计数为0后，调用对象的del方法(若存在的花)，然后释放对象的内存。

## 弱引用(Weak Reference)

弱引用的一个常用场景是缓存。一般地，我们不能因为一个对象再缓存中被引用就阻止对象呗回收。

```python
# please run in python console
import weakref
a_set = {0,1}
wref = weakref.ref(a_set)
wref
wref()
a_set = {2,3,4}
wref()
wref() is None
wref() is None
```

### 弱值词典(WeakValueDictionary)

弱值词典一般用来处理缓存。当其中的对象被回收后，词典对应的Key会自动从弱值词典中移除。

还有一个弱键词典(`WeakKeyDictionary`)，即：键值为弱引用。

> 弱键词典可以用来关联额外的数据，而无需在对象上添加这些数据为对象属性。

### 弱引用的局限性

不是所有的对象都可以作为弱引用的目标或指示对象(referent)，比如：列表(list)和词典(dict)对象。但是可以通过他们的自定义子类达到这个目的。

```python
class MyList(list):
    ''' list subclass whose instances may be weakly referenced '''

a_list = MyList(range(10))
# a_list can be the target of a weak reference
import weakref
wref_to_list = weakref.ref(a_list)
```

## 不可变类型的小技巧

对于不可变类型，python在生成对象时，可能会重用内存(不同的python实现会有不同)。

```python
##### tuple
t1 = (1,2,3)
t2 = tuple(t1)
t2 is t1 # True
t3 = t1[:]
t3 is t1 # True
t4 = (1,2,3)
t4 is t1 # False
##### str
s1 = 'ABC'
s2 = 'ABC'
s2 is s1 # True
```

