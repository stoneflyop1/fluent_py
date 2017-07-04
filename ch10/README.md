# 序列的技巧、哈希以及切片(Sequence Hacking, Hashing, and Slicing)

以一个多维的向量为例：

- 实现基本的序列协议：`__len__`以及`__getitem__`，Duck Typing
- 安全的字符串展示
- 恰当的切片支持，生成新的Vector实例
- 聚合所有包含的元素值的哈希
- 自定义格式化扩展

## Vector：一个用户定义的序列类型