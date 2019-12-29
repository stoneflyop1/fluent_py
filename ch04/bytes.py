cafe = b'caf\xc3\xa9' 
#cafe = bytes('café', encoding='utf_8') # bytes can be built from a str, given an encoding.
print(cafe.decode(encoding='utf8'))
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

import array
numbers = array.array('h', [-2,-1,0,1,2])
octets = bytes(numbers)
print(octets)

##########################
# struct and memoryview
import struct
fmt = '<3s3sHH' # struct format: < little-endian; 3s3s 两个三字节序列; HH：两个十六进制整数
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10] # header shares memory with img
print(bytes(header)) # copy bytes
print(struct.unpack(fmt, header))
del header
del img