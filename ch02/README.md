# 序列(Sequences)

字符串(Strings)、列表(lists)、字节序列(byte sequences)、数组(arrays)、XML元素、以及数据库的查询结果共用了很多通用操作，比如：迭代(iteration)、切片(slicing)、排序(sorting)以及拼接(concatenation)。

## 内置序列类型概要

- 作为[容器](https://docs.python.org/3/library/collections.abc.html)的序列(__container sequences__)：list, tuple以及collection.deque等，保存的是引用(hold references)
- 顺序结构(__flat sequences__)：str, bytes, bytearray, memoryview以及array.array等，保存的是值(store values)

另一种分组方式是基于对象是否可变分组，可变是指可以改变对象的内部状态或值，比如可以对序列中某一位置的元素进行重新赋值。

- 可变序列(__mutable sequences__)： list, bytearray, array.array, collections.deque以及memoryview
- 不可变序列(__immutable sequences__)：tuple, str以及bytes

关于容器和序列的关系可以参考如下的代码示例：

```python
class Container:
    def __contains__(self): pass

class Iterable:
    def __iter__(self): pass

class Sized:
    def __len__(self): pass

class Sequence(Container, Iterable, Sized):
    def __getitem__(self, index): pass
    def __reversed__(self): pass
    def index(self): pass
    def count(self): pass

class MutableSequence(Sequence):
    def __setitem__(self, index): pass
    def __delitem__(self, index): pass
    def insert(self, obj): pass
    def append(self, obj): pass
    def reverse(self): pass
    def extend(self, otherSequence): pass
    def pop(self): pass
    def remove(self, obj): pass
    def __iadd__(self, obj): pass
```


## 列表推导(List Comprehensions)以及生成器表达式(Generator Expressions)

列表推导用来生成列表，会在内存中生成列表对象实例并填充所有数据。列表推导使用中括号。基本形式如下：

```python
def map_fun(i): return i
list_obj = [1,2,3]
res = [map_fun(s) for s in list_obj]
```

列表推导相关示例代码见[listcomps.py](listcomps.py)

### 列表推导更加具有可读性

```python
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols: # use for...in adding item to a list
    codes.append(ord(symbol))
print(codes)
codes = [ord(symbol) for symbol in symbols] # use listcomp
print(codes)
```

注：python2.x版本中，列表推导不会建立局部作用域，若其中使用了当前作用域的其他变量名，则会修改其他变量的值；python3中无此问题(列表推导会创建局部作用域)。

```python
x = 'my precious'
dummy = [x for x in 'ABC']
# print x # x is 'C' in python2.x
print(x) # x is 'my precious' in python3
```

### 与过滤(filter)和映射(map)比较

如下示例对同一问题给出了listcomp和filter/map两种实现方式。filter和map将在[ch05](/ch05/)中详细介绍。

```python
symbols = '$¢£¥€¤'
# 列表推导实现
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
# 过滤和映射
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
```

### 笛卡尔积(Cartesian Products)

```python
#笛卡尔积,两两结合的tuple列表
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for color in colors:
    for size in sizes:
        print((color, size))
tshirts = [(color, size) for color in colors
                            for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes
                            for color in colors]
print(tshirts)
```

### 生成器表达式(Generator Expressions)

元组(tuples)、数组(arrays)以及其他类型的序列，也可以使用listcomp，但是生成器表达式(genexp)更加的节省内存，因为它使用迭代器协议(iterator protocol)来一项项添加到序列中(使用__yield__关键字)，而不会像listcomp那样先生成整个列表，再添加到序列。genexps是懒加载方式(延后加载)，listcomps是热加载方式(立即加载)。

genexps唯一与listcomps不同的地方是使用小括号`()`而不是中括号`[]`。

```python
# 生成器表达式
symbols = '$¢£¥€¤'
codes = tuple(ord(symbol) for symbol in symbols)
print(codes)
import array
generator = (ord(symbol) for symbol in symbols)
print(generator)
codes = array.array('I', generator)
print(codes)
```

## 元组(tuple)：不只是不可变的列表

元组相关示例代码见[tuple.py](tuple.py)

### 元组拆包(Tuple Unpacking)

- 给多个变量并行赋值(Parallel Assignment)
- 使用星号(*)把一个元组数据分成不同参数传给其他函数
- 函数通过返回一个tuple返回多个值
- 使用星号(*)捕获额外的多个值为列表
- 可以进行嵌套拆包(nested tuple unpacking)

```python
# Parallel Assignment
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE324567')]
for passort in sorted(traveler_ids): print('%s/%s' % passort)

# unpacking with star symbol
print(divmod(20,8))
t = (20,8)
print(divmod(*t))
quo, rem = divmod(*t)
print(quo, rem)

# return multi-value
import os
_, filename = os.path.split(__file__)
print(filename)

# star grab items
a,b,*rest = range(5)
print(a,b,rest)

# 嵌套拆包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
]
print('{:15} | {:^9} | {:^9}'.format('city.', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0 : print(fmt.format(name, latitude, longitude))
```

### 命名元组(Named Tuples)

命名元组是元组的子类(subclass)，增加了字段的名称(field names)以及类名(class name)属性。
跟自定义对象相比，它的好处是不需要在每个实例上存储一个`__dict__`，节省内存。适用于仅有数据的对象类定义。

```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # City(*delhi_data)
tDict = delhi._asdict() #OrderedDict
for key, value in tDict.items(): print(key+':', value)
```

### 元组作为不可变列表

| 方法 | list | tuple | 示例说明 |
| ---- | ---- | ---- | ---- |
| `s.__add__(s2)` | ✔ | ✔ | `s + s2` -- concatenation |
| `s.__iadd__(s2)` | ✔ | -- | `s += s2` -- in-place concat |
| `s.append(e)` | ✔ | -- | add element to the end |
| `s.clear()` | ✔ | -- | delete all items |
| `s.__contains__(e)` | ✔ | ✔ | `e in s` |
| `s.copy()` | ✔ | -- | shallow copy |
| `s.count(e)` | ✔ | ✔ | occurences of item e |
| `s.__delitem__(index)` | ✔ | -- | remove at index |
| `s.extend(it)` | ✔ | -- | append items of iterable  to the end |
| `s.__getitem__(index)` | ✔ | ✔ | `s[index]` |
| `s.index(e)` | ✔ | ✔ | find the first index of an item e |
| `s.insert(index, e) | ✔ | -- | insert e just before index |
| `s.__iter__()` | ✔ | ✔ | get iterator |
| `s.__len__()` | ✔ | ✔ | `len(s)` |
| `s.__mul__(n)` | ✔ | ✔ | `s*n` repeat concat |
| `s.__imul__(n)` | ✔ | -- | `s *= n` in-place |
| `s.__rmul__(n)` | ✔ | ✔ | `n*s` reversed repeat concat |
| `s.pop([index])` | ✔ | -- | remove and return last item or item at optional index |
| `s.remove(e)` | ✔ | -- | remove the first occurence of e by value |
| `s.reverse()` | ✔ | -- | in-place reverse |
| `s.__reversed__()` | ✔ | -- | get iter to scan from last to first |
| `s.__setitem__(index, e)` | ✔ | -- | `s[index] = e` |
| `s.sort([key], [reverse])` | ✔ | -- | in-place sort with optional key and order |

## 切片(Slicing)

### 切片对象(Slice Object)

使用`[start:stop:step]`生成切片，或使用切片对象。

```python
l = [1,2,3,4]
l[:2] # [1,2]
l[2:] # [3,4]
l[::2] # [1,3]
s = slice(0,2)
l[s] # [1,2]
```

### 多维切片(Multidimensional Slicing)和省略(Ellipsis)对象

多维切片的每一维都通过逗号(,)分隔。例如在numpy包中的numpy.ndarray，可以使用a[m:n,k:l]的方式生成切片。

省略对象通过三个点号(three full stops)表示(...)。例如：对于一个四维数组x，x[i,...] = x[i,:,:,:]。

### 给切片赋值

```python
l = list(range(10))
print(l)
l[2:5] = [20,30] # 仅会给2，3重新赋值
print(l)
```


## 在序列中使用+和*

示例代码见[op.py](op.py)

```python
[1,2]*2 # [1,2,1,2]
2*'ab' # 'abab'
```

### 创建包含列表的列表(nested lists)

使用`*`重复生成列表元素时，要注意若`*`操作的是引用(如：list)，则重复生成的list元素都是指向同一个地址的引用。

示例见[weird.py](weird.py)

```python
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'
print(weird_board) # [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
# same as below
row = ['_'] * 3
board = []
for i in range(3): board.append(row)
```

### 序列的增量赋值(Augmented Assignment)

- `__iadd__` (对于可变类型为在位编辑) => +=  if not mutable, use `__add__` (重新赋值)
- `__imul__` (对于可变类型为在位编辑) => *=

建议：不要在tuple中使用可变对象。

## 排序(list.sort和sorted函数)

`list.sort`方法使用在位(in-place)排序的方式; `sorted`内置函数则会生成一个新的列表。
两个方法都接受两个可选参数：

- `reverse`: 默认为False，若为True，则降序排列
- `key`：接受一个参数的函数，默认函数为返回元素本身(identity function)，即：用元素本身做比较

示例见[sort.py](sort.py)

```python
l = [3,5,1,8]
l2 = sorted(l) # l2 = [1, 3, 5, 8], l = [3,5,1,8]
l.sort(reverse=True) # l = [8, 5, 3, 1]
```

## [有序序列的二分查找](https://docs.python.org/3/library/bisect.html)

若序列有序，可以使用二分查找(bisect.bisect)提高查询速度(时间复杂度是：ln N);若插入元素到序列需要保持顺序，可以使用`bisect.inorder进行插入操作。示例见：[bisect_test.py](bisect_test.py)。

## 何时不需要使用list

- 存储大量的浮点数时用数组(array)更高效
- 若经常性的要在序列两端添加或删除元素，则使用deque(双端队列)更合适 
- 若需要经常判断元素是否在序列中，可以使用集合(set)。

## 可变序列

示例代码见[nolist.py](nolist.py)

### [数组(array)](https://docs.python.org/3/library/array.html)

类似于C语言中的数组，数组中的元素类型相同，存储更紧凑，相比list更节省空间。

### [内存视图(Memory View)](https://docs.python.org/3/library/stdtypes.html#memory-views)

内存视图是一种共享内存的的序列类型，可以用来处理数组切片。
关于何时应该使用内存视图的讨论可以参考[Stackoverflow上的讨论](https://stackoverflow.com/questions/4845418/when-should-a-memoryview-be-used/)：
> 一个内存视图基本上就是python中的一个广义的numpy中的数组结构(没有数学部分)。它允许你在数据结构中共享内存而不需要拷贝。这对于大的数据集非常重要。

```python
# memoryview, 通过修改字节修改数组的值
numbers = array('h', [-2,-1,0,1,2]) # 有符号的整数(符号占用一个位)：signed integer
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B') # 内部表示改为字节(byte)形式，注：每8个位(bit)为一个字节，每个位只有0，1两种值
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
```

要切换内存视图的表示，可以通过memoryview.cast方法切换内存表示，如：从h(short signed integer)换成B(unsigned char)。

### 队列

使用序列上的__append__和__pop__方法可以用来模拟栈(stack, 先进后出：FILO)和队列(先进先出：FIFO)这两种数据结构。
collections.deque是一个线程安全的两端队列，可以在两端进行插入和删除操作。

## 小结

- 序列通常按照可变和不可变区分，但也可以按照顺序结构(flat)和容器(container)序列来分。顺序结构更紧凑、快、易于使用，但仅能保存原子数据(atomic)，比如：数字、字符、字节；容器序列更灵活，但是当它们的元素是可变对象时，会有意想不到的结果，尤其是有嵌套数据结构的时候。
- 列表推导和生成表达式是一种很强大的生成序列的方式，比用遍历的方式更直观。
- 元组可以作为未命名字段的记录以及不可变的列表。元组拆包可以用来给多个变量赋值，甚至可以指定某个变量获得一个元组部分元素的列表值。
- 序列切片和省略[ellipsis (...)]也是很强大的工具，具体使用可以参考numpy包。

