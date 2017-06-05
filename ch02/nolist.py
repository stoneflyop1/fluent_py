
######################
# 创建、保存以及加载大型的浮点数数组
from array import array
from random import random
num = 10**5
floats = array('d', # 创建double类型的数值数组
    (random() for i in range(num)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp) # 写入二进制文件
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, num) # 从二进制文件中读取数组内容
fp.close()
print(floats2[-1])
print(floats2 == floats) # True，感觉应该是按值按顺序比较

#############################
# memoryview, 通过修改字节修改数组的值
numbers = array('h', [-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

################################
# deque
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11,22,33])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)