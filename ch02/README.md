# 序列(Sequences)

字符串(Strings)、列表(lists)、字节序列(byte sequences)、数组(arrays)、XML元素、以及数据库的查询结果共用了很多通用操作，比如：迭代(iteration)、切片(slicing)、排序(sorting)以及拼接(concatenation)。

## 内置序列类型概要

- 作为容器的序列(`container sequences`)：list, tuple, collection.deque等，保存的是引用(hold references)
- 单一序列(`flat sequences)`：str, bytes, bytearray, memoryview以及array.array等，保存的是值(store values)

另一种分组方式

- 可变序列(`mutable sequences`)： list, bytearray, array.array, collections.deque以及memoryview
- 不可变序列(`immutable sequences`)：tuple, str以及bytes

## 列表推导(List Comprehensions)以及生成器表达式(Generator Expressions)

列表推导用来生成列表，会在内存中生成列表对象实例并填充所有数据。

列表推导相关示例代码见[listcomps.py](listcomps.py)

### 列表推导更加具有可读性

```python
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols: #使用for...in添加列表项
    codes.append(ord(symbol))
print(codes)
codes = [ord(symbol) for symbol in symbols] # 使用列表推导直接生成列表
print(codes)
```

注：python2.x版本中，列表推导中的变量若与当前作用域(scope)内的变量名相同，执行列表推导后，变量会跟列表推导中的值相同；python3中无此问题(列表推导会创建局部作用域)。

```python
x = 'my precious'
dummy = [x for x in 'ABC']
print x # x is 'C' in python2.x
print(x) # x is 'my precious' in python3
```

### 与过滤(filter)和映射(map)比较

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

元组(tuples)、数组(arrays)以及其他类型的序列，也可以使用listcomp，但是生成器表达式(genexp)更加的节省内存，因为它使用迭代器协议(iterator protocol)来一项项添加到序列中，而不会像listcomp那样先生成整个列表，再添加到序列。

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

## 元组(tuple)不只是不可变的列表

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
跟自定义对象相比，它的好处是不需要在每个实例上存储一个`__dict__`，节省内存。

```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
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

## 切片(Slicing)

### 切片对象(Slice Object)

使用`[start:stop:step]`生成切片对象。

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

### 使用列表创建列表

```python
l = [1,2,3]
print(l*3) # [1,2,3,1,2,3,1,2,3]
print(2*'abcd') # 'abcdabcd'
```
注：若序列中的元素为引用类型(如：元素为列表),则新生成的序列中引用类型虽然展示多个，但其实都是指向同一个内存地址。因为作为容器的序列中保存的是引用，而不是数据。

### 序列的增量赋值(Augmented Assignment)

- `__iadd__` (对于可变类型为在位编辑) => +=  if not, use `__add__` (重新赋值)
- `__imul__` (对于可变类型为在位编辑) => *=

## 排序(list.sort和sorted函数)

`list.sort`方法使用在位排序的方式，而`sorted`内置函数则会生成一个新的列表。
两个方法都接受两个可选参数：

- `reverse`: 默认为False，若为True，则降序排列
- `key`：接受一个参数的函数，默认函数为返回元素本身(identity function)，即：用元素本身做比较
