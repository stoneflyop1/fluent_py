# python对象

- 使用内置函数自定义对象表示(如：repr(), bytes()等)
- 实现一个可选的构造器作为类方法
- 扩展对象的字符串格式化(str.format)
- 提供对象的只读属性
- 对象的哈希
- 使用`__slots__`节省内存

## 对象表示(Object Representations)

代码示例见：[vector2d.py](vector2d.py)

- `__repr__` -> `repr()` => 开发者友好的字符串表示
- `__str__`  -> `str()`  => 用户友好的字符串表示
- `__bytes__` => 字符序列表示
- `__format__` -> `format()` or `str.format()` => 格式化字符串

## 一个可选的构造函数

- 类方法(`classmethod`)：第一个参数为类的类型(一般命名为：`cls`)，比如：Vector2d。
- 静态方法(`staticmethod`)：没有占位参数，使用场景不多，一般可以用函数代替

代码示例见：[methoddemo.py](methoddemo.py)