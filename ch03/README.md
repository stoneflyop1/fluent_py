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