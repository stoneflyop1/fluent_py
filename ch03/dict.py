# generic Mapping type
import collections
from collections import Mapping # from collections.abc if 2.6~3.2
my_dict = {}
print('Is dict Mapping type? '+str(isinstance(my_dict, Mapping)))

# create a dict
a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'],[1,2,3]))
d = dict([('two',2), ('one', 1), ('three',3)])  # dict Comprehension
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e) # True

# get default value for dict and setdefault for a key
d = {}
getdefault = 2
print(d.get(1, getdefault))
print(d.__contains__(1)) # False
d.setdefault(2, 3)
print(d[2]) # 3

dd_type = list
dd = collections.defaultdict(dd_type)
dd[0] = 1
print(dd[0])
print(dd[1])