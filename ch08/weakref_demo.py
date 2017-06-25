import weakref
##############################
# del not delete objects
s1 = {1,2,3}
s2 = s1
def bye(): print('Gone with wind...')
ender = weakref.finalize(s1, bye)
print(ender.alive) # True
del s1 # alive even the name is deleted
print(ender.alive) # True
s2 = 'spam' # rebinded, object freed
print(ender.alive) # False

a_set = {0,1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2,3,4}
print(wref())
print(wref() is None)

#################################
# 弱值词典
print('###############################')
print('demo weakvaluedict')
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
            Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog: stock[cheese.kind] = cheese
print(repr(sorted(stock.keys()))) # if not use repr, will print a generator object
del catalog
print(repr(sorted(stock.keys())))
del cheese # local variable in global
print(repr(sorted(stock.keys())))

## subclass list to generate weakreference target
class MyList(list):
    ''' list subclass whose instances may be weakly referenced '''
a_list = MyList(range(10))
# a_list can be the target of a weak reference
wref_to_list = weakref.ref(a_list)
print(wref_to_list)