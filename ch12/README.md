# 继承：好，还是坏？ (Inheritance: For Good or For Worse)

## 内置类型派生子类要小心(Subclassing Built-In Types Is Tricky)

内置类型是C实现的，不建议直接从内置类型派生子类，容易出问题。python实现的类则基本无此问题。

> 内置类型如：dict, list或者str等直接做派生比较容易出错，因为内置方法大部分都会忽略自定义的重载。建议从collections模块中的类进行派生，如：UserDict, UserList以及UserString，它们就是用来进行扩展的。

## 多继承和方法解析顺序(Multiple Inheritance and Method Resolution Order)

如下代码中的继承关系，若调用D上的方法，则查找顺序为D->B->C->A。

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
```