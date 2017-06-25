# python对象

- 使用内置函数自定义对象表示(如：repr(), bytes()等)
- 实现一个可选的构造器作为类方法
- 扩展对象的字符串格式化(str.format)
- 提供对象的只读属性
- 对象的哈希
- 使用`__slots__`节省内存

## 对象表示(Object Representations)

- `__repr__` -> `repr()` => 开发者友好的字符串表示
- `__str__`  -> `str()`  => 用户友好的字符串表示
- `__bytes__` => 字符序列表示
- `__format__` -> `format()` or `str.format()` => 格式化字符串