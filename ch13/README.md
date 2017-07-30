# 运算符重载(Operator Overloading)

- Python如何对不同类型的操作对象支持infix运算符
- 使用鸭子类型或显示地类型检查处理不同类型的操作对象
- infix操作符应该如何提示它无法操作一个操作对象
- 比较操作符的特殊行为
- 增量赋值操作符(augmented assignment oeprators，比如：+=)的默认处理，以及如何重载

## 101

- 内置类型无法进行操作符重载
- 无法创建新的操作符
- 有几个操作符无法被重载，如：is, and, or, not；但对应的移位操作可以重载

## Unary操作符

- `__neg__` -> -
- `__pos__` -> +
- `__invert__` -> ~  (对整数按位取反)

## infix +

a+b:

1. 若a实现了`__add__`，会调用`a.__add__(b)`
1. 若a未实现`__add__`，会检查b是否实现了`__radd__`，并调用之
1. 若b未实现`__radd__`，会出发TypeError

## Rich Comparison Operators

Group | Infix Operator | Forward method call | Reverse method call | Fall back
----  |      ----      |        ----         |          ----       |   ----
Equality | a == b | `a.__eq__(b)` | `b.__eq__(a)` | Return id(a) == id(b)
         | a != b | `a.__ne__(b)` | `b.__ne__(a)` | Return not (a == b)
Ordering | a > b  | `a.__gt__(b)` | `b.__lt__(a)` | Raise TypeError
         | a < b  | `a.__lt__(b)` | `b.__gt__(a)` | Raise TypeError
         | a >= b | `a.__ge__(b)` | `b.__le__(a)` | Raise TypeError
         | a <= b | `a.__le__(b)` | `b.__ge__(a)` | Raise TypeError

## 增量赋值操作符

不要对不可变类型实现增量赋值操作符。