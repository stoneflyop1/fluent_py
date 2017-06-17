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

示例代码见：[bytes.py](bytes.py)

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


## 文本编码和解码

文本是可以按照不同的编码器以不同的字节序列进行编码的，解码即通过编码器把字节序列重新还原为文本。

常用的编解码器是 `utf-8`，python中的编解码器名称为`utf_8`。

- `utf_*`系列的编码器可以用在所有文本上，而像`latin_1`或`iso8859_1`这种编码器对某些字符会抛出`UnicodeEncodeError`，比如：中文。
- 从文本到字节进行解码时，若文本中有些字符的编码无法使用给出的编码器来解释，则会触发`UnicodeDecodeError`
- 若出现了import文件时的编码问题，可以在py文件里指定文件编码；py文件的默认编码主要是utf-8。

    ```python
    # coding: gb2312
    ```
- 无法直接从字符序列中推导出编码，只能指定编码。比如：网络请求中获取反馈时一般反馈头会给出编码。若只能通过推导得出编码，可以使用[Chardet](https://pypi.python.org/pypi/chardet)包。
- BOM(byte-order mark)是不可见字符，UTF-16支持。Windows平台的UTF-8编码也有是否带有BOM的区分。


## 处理文本文件

- bytes -> str: 输入字节，解码为文本 (如：接收网络传输的内容)
- str: 纯文本处理
- str -> bytes: 编码为字节，输出(如：网络请求的内容传输)

注：Windows系统下的文件系统编码问题解释：[Difference between MBCS and UTF-8 on Windows](https://stackoverflow.com/questions/3298569/difference-between-mbcs-and-utf-8-on-windows)

## Unicode正则化(normalization)

- NFC(Normalization Form C)会组合字符的码位(code point)以生成最短的等价字符串
- NFD会把字符展开成基本字符(base characters)
- NFKC和NFKD中的K表示相容性(compatibility)，对于compatibility字符会进行相融分解(compatibility decomposition)，即使会有格式损失。

## 对Unicode文本排序

### 本地化排序，使用`locale.strxfrm`

使用前，需要调用 `setlocale(LC_COLLATE, language_code.encoding)`指定本地化编码

- locale设置是全局的，不建议在程序使用中调用setlocale方法
- 要设置的locale必须在OS中以安装，否则会出发locale.Errror异常
- 必须知道完整的locale名字，Unix下的名字格式： `language_code.encoding`
- 不同OS上locale实现可能不同，会有不同的效果，比如：MacOS就无效

### Unicode Collation算法(UCA)

UCA算法的好处是不考虑locale，且可以提供自己的Collation表。

需要使用pip安装pyuca库

```sh
pip3 install pyuca
```

## Unicode数据库

Unicode标准提供了一个完整的数据库，由多个结构化的文本文件给出。其中不仅仅给出了字符名称的码位映射，还给出了单个字符的元数据，以及它们是如何关联的。比如：Unicode数据库中的记录会告诉我们一个字符是否是可打印的(`printable`)、一个字母(`letter`)、十进制数、或者其他数值符号等。`str`上的`isidentifier`、`isprintable`、`isdecimal`和`isnumeric`如何工作的；str.casefold也用到了Unicode表的信息。

示例代码中的输出：(unicode数据:  1¼²३፫Ⅻ⑦⒀㊅)

| `Code Point` | `representation` | `re_digit` | `str_isdig` | `str_isnum` | `numeric float` | `unicode name` |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| U+0031 |  1  | re_dig | isdig | isnum  | 1.00  | DIGIT ONE |
| U+00bc |  ¼  |   -   |   -  |   isnum  | 0.25 | VULGAR FRACTION ONE QUARTER |
| U+00b2 |  ²  |   -   |  isdig |  isnum  | 2.00 | SUPERSCRIPT TWO |
| U+0969 |  ३  | re_dig | isdig |  isnum  | 3.00 | DEVANAGARI DIGIT THREE |
| U+136b |  ፫  |   -   |  isdig |  isnum  | 3.00 | ETHIOPIC DIGIT THREE |
| U+216b |  Ⅻ  |   -   |   -   |  isnum  | 12.00 | ROMAN NUMERAL TWELVE |
| U+2466 |  ⑦  |   -   | isdig |  isnum  |  7.00  | CIRCLED DIGIT SEVEN |
| U+2480 |  ⒀  |   -   |   -   |  isnum  | 13.00 | PARENTHESIZED NUMBER THIRTEEN |
| U+3285 |  ㊅  |   -   |   -   |  isnum  |  6.00  | CIRCLED IDEOGRAPH SIX |

## 双模式的字符串和字节API

### 正则表达式

匹配数字和文字时，若正则表达式的pattern以str形式给出，则可以匹配unicode形式的数字和字母；若以byte形式给出(b模式)，则只匹配ASCII字符。

str形式的pattern情况下，有一个`re.ASCII`的标志使得 `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`和`\S`仅匹配ASCII字符。

### 系统函数(os function)

os函数接受文件名或路径名为str或者byte模式，得出的结果跟文件系统的编码有关(sys.getfilesystemencoding)。byte模式下对于需要编码的字符会给出其码位。

```python
“>>> os.listdir('.')  # 
['abc.txt', 'digits-of-π.txt']
>>> os.listdir(b'.')  # 
[b'abc.txt', b'digits-of-\xcf\x80.txt']”
```

os模块还提供了两个专门的编码解码函数，其中参数filename即可以使str，也可以使byte

- fsencode(filename)：若filename为str，则编码为byte
- fsdecode(filename)：若filename为byte，则解码为str