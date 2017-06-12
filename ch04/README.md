# 文本vs.字节(Text versus Bytes)

- 字符(Characters)，码位(code points)，字节表示(byte representations)
- 二进制序列的唯一特性：字节(bytes)，字节数组(bytearray)，内存视图(memoryview)
- 完整的Unicode(full Unicode)以及遗留字符集的编码(Codecs)
- 避免和处理编码错误(encoding errors)
- 处理文本文件的最佳实践
- 默认编码陷阱(encoding trap)和标准的I/O问题
- 正规化(normalization)的安全的Unicode文本比较
- 正规化(normalization)、大小写处理(case folding)以及蛮力读音符号删除(diacritic removal)的通用函数
- 使用本地化方式对Unicode文本进行正确的排序和PyUCA库
- Unicode数据库中的字符元数据
- 处理str和bytes的双模式API

## 字符问题

示例代码见[char.py](char.py)

字节现在一般指Unicode字符，Python3中的str就是Unicode字符串，与Python2中的unicode对象类似。注意：Python2中的str得到的是未经处理的字节。

### 字符的编码(encode)和解码(decode)

编码：从字符到码位，需要制定编码格式，如：utf8
解码：从码位到字符，需要制定编码格式，如：utf8

## 字节基础

Python3中的`bytes`并不仅仅是python2中的`str`。

- 不可变字节： `bytes`
- 可变字节数组： `bytearray`

字节数组的字面值表示

- 可打印的ASCII
- 转义序列，如：制表符(tab)、换行符(newline)、回车符(carriage return)、以及转义字符(\)
- 所有其他的字节值使用16进制的转义序列(如：\x00表示空字节)

创建字节数组

- 使用fromhex方法 如：bytes.fromhex('31 4B CE A9')
- 使用构造函数
    - str类型的参数以及encoding关键词变量
    - 可遍历集合(元素范围：0~255)
    - 一个实现了缓冲的协议(buffer protocol)，如：bytes, bytearay, memoryview, array.array)

注：使用buffer-like源对象创建字节数组会进行一次拷贝；而memoryview则可以跟源共享内存

## 结构和内存视图

结构(struct)模块可以解析字节数组为不同类型的字段组成的元组，或者从元组包装成(pack)字节数组。


