symbols = '$¢£¥€¤'

# 使用列表推导直接生成列表(映射)
codes = [ord(symbol) for symbol in symbols] 
print(codes)
# 过滤
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
# 使用filter和map
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

#笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for color in colors:
    for size in sizes:
        print((color, size))
tshirts = [(color, size) for color in colors
                            for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes
                            for color in colors]
print(tshirts)

# 生成器表达式
codes = tuple(ord(symbol) for symbol in symbols)
print(codes)
import array
generator = (ord(symbol) for symbol in symbols)
print(generator)
codes = array.array('I', generator)
print(codes)

