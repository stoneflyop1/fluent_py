# 序列的技巧、哈希以及切片(Sequence Hacking, Hashing, and Slicing)

以一个多维的向量为例：

- 实现基本的序列协议：`__len__`以及`__getitem__`，Duck Typing
- 安全的字符串展示
- 恰当的切片支持，生成新的Vector实例
- 聚合所有包含的元素值的哈希
- 自定义格式化扩展


## 序列

### Vector：一个用户定义的序列类型

与Vector2d不同，我们接受一个序列作为构造参数。

### 优化切片操作

通过传入的参数不同，返回不同的对象，若传入整数，则返回对应位置的序列中的值；若传入的是下标切片，则返回对应的一个Vector实例。

### 使用动态属性(Dynamic Attribute Access)

