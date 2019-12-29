# generic Mapping type
import collections
from collections.abc import Mapping # py > 2.6
my_dict = {}
print('Is dict Mapping type? '+str(isinstance(my_dict, Mapping)))

# create a dict
a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'],[1,2,3]))
d = dict([('two',2), ('one', 1), ('three',3)])  # dict Comprehension
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e) # True
# dictcomps
f = {code: country for code, country in [(86,'China'), (91, 'India')]}

# get default value for dict and setdefault for a key
d = {}
default = 2
print(d.get(1, default))
print(d.__contains__(1)) # False
d.setdefault(2, 3)
print(d[2]) # 3

dd = collections.defaultdict(list)
dd[0] = 1
print(dd[0]) # 1
print(dd[1]) # []

# # ChainMap
# import builtins
# pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
# print(pylookup)

# Counter
ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaaazzzzz')
print(ct)
print(ct.most_common(2))

############################################
# str key dict with __missing__ method
## subclass dict
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str): # If key is str, and it’s missing, raise KeyError.
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key] # __getitem__, will call __missing__ method if key is missing
        except KeyError:
            return default
    
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

## subclass UserDict, no need to implement get method, use Mapping.get
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

## dict sorting
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55,'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
d1 = dict(DIAL_CODES)
print('d1: ', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2: ', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3: ', d3.keys())
assert d1 == d2 and d2 == d3