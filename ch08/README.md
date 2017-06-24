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