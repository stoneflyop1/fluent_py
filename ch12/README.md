# 继承：好，还是坏？ (Inheritance: For Good or For Worse)

## 内置类型派生子类要小心(Subclassing Built-In Types Is Tricky)

内置类型是C实现的，不建议直接从内置类型派生子类，容易出问题。python实现的类则基本无此问题。

> 内置类型如：dict, list或者str等直接做派生比较容易出错，因为内置方法大部分都会忽略自定义的重载。建议从collections模块中的类进行派生，如：UserDict, UserList以及UserString，它们就是用来进行扩展的。

## 多继承和方法解析顺序(Multiple Inheritance and Method Resolution Order)

如下代码中的继承关系，若调用D上的方法，则查找顺序为D->B->C->A。即：方法解析顺序(MRO)除了跟继承类的链图顺序有关，还跟子类定义时引入的父类(superclasses)顺序有关。

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
```

## 处理多继承

### 1. 区分接口继承和实现继承

- 接口继承(Inheritance of interface)创建一个子类型，蕴含了"is-a"关系
- 实现继承(Inheritance of implementation)是为了重用，避免重复编码

### 2. 接口要显示地作为抽象基础类(Make Interfaces Explicit with ABCs)

对于Python3.4以上版本，实现abc.ABC子类，或在低版本中的python中其他的ABC类。

### 3. 使用Mixins以方便代码重用

为了重用代码，如果方法实现时用到的参数可能来自于不相关的子类实例，则应该显示声明为`mixin class`。从概念上来说，mixin没有定义一个新的类型，它仅仅组合一些方法用于重用。

### 4. 显示命名Mixin类(Make Mixins Explicit by Naming)

python中没有官方的方式声明一个类为mixin，因此强烈建议参数命名时添加Mixin后缀。

### 5. ABC可能是一个Mixin，但是Mixin可能不是ABC

因为ABC可以不仅仅包含抽象方法，可以实现具体的方法。ABC也定义了类型，且可以被继承。

### 6. 不要子类化多于一个的具体类(Concrete Class)

### 7. 提供聚类(Aggregate Classes)给用户

若ABC或mixin的一些组合特别有用，可以用一个聚类把他们组合起来提供给用户。

### 8. 优先使用对象组合而不是类继承