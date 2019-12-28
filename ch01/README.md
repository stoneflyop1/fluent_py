# Python数据模型

## python中的特殊方法(special methods)

以双下划线开始和结尾的方法在Python中是称作特殊方法(**special method**)，可以用于相关的任何对象。比如：`__getitem__`可以用于集合(collections)、迭代(iteration)，以及属性访问(attribute access)中。下面的卡片组示例演示了如何在自己的类中使用特殊方法。
注：因为以双下划线开始和结束，也称为**dunder methods**。

## python方式处理卡片组(Card Deck)

使用特殊方法 `__getitem__`和`__len__`实现序列(sequence)，鸭子类型。详细示例参见[示例1](example1.py)

## 如何使用特殊方法

特殊方法直接由Python解释器调用，比如：`__len__`方法会通过`len`函数调用，`__getitem__`通过`[]`调用。

对于内置类型，如：list, str, bytearray等，Python对`len()`的实现是返回的PyVarObject的C结构体的ob_size字段值；因此速度非常快。

`for i in obj`操作会调用对象obj上的`__iter__`特殊方法，如果存在的话。

### 特殊方法的使用

- 除非进行元编程，否则不要直接调用特殊方法。
- 唯一的例外是`__init__`方法，用来对父类进行初始化。
- 可以使用内置函数(len, iter, str等)触发特殊方法的调用
- 不要自创`__foo__`特殊方法，因为将来某些特殊方法会有特殊的含义

## 模仿数值类型

可以重载数学运算符以及相关的方法来实现模仿数值类型的目的。常用算术运算符如下：

- `__add__` => +
- `__sub__` => -
- `__mul__` => *
- `__truediv__` => /
- `__mod__` => %
- `__abs__` => abs
- `__neg__` => -
- `__pos__` => +


详细的示例见[示例2](example2.py)

### 字符串表示

- 交互环境以及调试器中都会调用repr特殊方法来展示表达式的值。**__repr__**的默认实现为输出对象的名称以及在内存中的地址。例如：`<Vector object at 0x10e1000070>`
- **print**函数内部隐式的调用了`__str__`特殊方法，若未实现此方法，Python解释器会调用`__repr__`方法


### 转换对象为bool值

对象可以直接在条件语句使用中，其真(True)或假(False)的值有如下顺序规则：

1. 若实现了`__bool__`的特殊方法(内置方法为bool)，返回此方法的值
2. 若实现了`__len__`，返回 **len(obj) != 0**
3. 返回True

## 本章小结

通过实现特殊方法，自定义类就可以像内置类型那样使用。

- 一般地，[Python对象需要提供一个字符串表示的形式](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)，可以用于调试和日志输出(**repr**)，或提供给终端用户查看(**str**)。
- 特殊方法经常用来模拟序列、数值类型等

