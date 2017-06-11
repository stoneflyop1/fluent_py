# 词典和集合

词典(dict)和集合(set)都是通过哈希表(hashtable)实现的。

## 词典

示例代码见[dict.py](dict.py)。

### 一般的映射(Mapping)类型

collections(python2.6~3.2中为collections.abc)中的Mapping和MutableMapping给出了词典和相似类型的统一接口形式。

```python
# generic Mapping type
from collections import Mapping # from collections.abc if 2.6~3.2
my_dict = {}
print(isinstance(my_dict, Mapping)) # True
```

python中的hashtable需要实现两个特殊方法：`__hash__`(用来生成不可变的散列值)和`__eq__`(用来比较相等)。所有原子非可变类型(atomic immutable type)，比如：字符串、字节、数值类型都是可哈希的。对于集合类型，需要其中的元素都是可哈希的。

注：用户自定义类型有默认的`__hash__`实现，那就是`id()`。

实例化词典

```python
a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'],[1,2,3]))
d = dict([('two',2), ('one', 1), ('three',3)]) # dict Comprehension
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e) # True
```

可以使用setdefault参数指定未找到时的默认值，并把默认值写入词典。get方法的第二个参数不会写入词典。

```python
d = {}
getdefault = 2
print(d.get(1, getdefault))
print(1 in d) # False
d.setdefault(2, 3)
print(d[2]) # 3

```

也可以使用collections.DefaultDict(default_type)生成词典，当访问到还未添加的Key时，自动生成Key的默认值。

```python
dd_type = list
dd = collections.defaultdict(dd_type)
dd[0] = 1
print(dd[0]) # 1
print(dd[1]) # []
```

也可以使用特殊方法`__missing__`，需要注意的是：此方法只在`__getitem__`方法和`indexer([])`中有会被调用，而`get`和`__contains__`(in)不会调用它。

注意：python3可以有效的使用` key in d.keys() `方法判断一个key是否在词典中，因为d.keys()得到的是一个集合(set)；而python2中因为d.keys()得到的是一个列表，所以效率会非常低。

### 词典的变种

- 排序词典(collections.OrderedDict)：会记住Key插入的顺序
- 链映射(collections.ChainMap)：把多个词典链接到一起
- 计数器(collections.Counter)：按照列表元素作为Key进行计数
- 用户词典(collections.UserDict)：一个一般化的词典，用来用户自定义词典，其子类与dict对象类似

### 不可变映射

py3.3 引入了`types.MappingProxyType`类，可以作为不可变映射使用。


## 集合(set)

与数学中的集合概念类似，集合中没有重复的元素。

```python
>>> l = ['spam', 'spam', 'eggs', 'spam']
>>> set(l)
{'eggs', 'spam'}
>>> list(set(l))
['eggs', 'spam']
```

集合有并(union, |)、交(intersection, &)、差(difference, -)等操作，与数学上的操作类似。

集合也有像列表推导一样的集合推导(set comprehension)，简称：setcomps。

## 词典和集合如何实现

几个问题：

- 词典和集合效率有多高？
- 为什么不能保持顺序？
- 为什么不能把任意的对象作为词典的键值或集合中的元素？
- 为什么词典的键值和集合元素的顺序会依赖于插入顺序，且会随着这两种结构的生命周期变化？
- 为什么在遍历词典和集合时给它们添加其他元素是一个馊主意？

### 词典中使用哈希

#### 键值必须是可哈希的对象

1. 具有hash()方法，且此方法返回的哈希值在对象的生命周期保持一致
1. 对象可判断相等，通过eq()方法
1. 若`a == b`，则 `hash(a) == hash(b)`

注意：

- 用户自定义的类型都是可哈希的，因为hash方法会返回id()方法的值，且所有的自定义类型id()的值都是不相等的。
- 若自定义类实现了`__eq__`方法，则必须也实现一个适当的`__hash__`方法，否则会打破可哈希对象的第三条特征。


其他

- 词典的内存效率不高，因为内部有一个稀疏的哈希表
- 键值查找很快
- 键值排序依赖于插入序
- 向词典添加新项可能改变已存在的键值顺序
