# tuple unpacking

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # Parallel Assignment
print(latitude)
print(longitude)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE324567')]
for passort in sorted(traveler_ids): print('%s/%s' % passort)
print(divmod(20,8))
t = (20,8)
print(divmod(*t)) # unpacking with star symbol
quo, rem = divmod(*t)
print(quo, rem)
# 函数返回多值
import os
_, filename = os.path.split(__file__)
print(filename)

# star grab items
a,b,*rest = range(5)
print(a,b,rest)
a,b,*rest = range(2)
print(a,b,rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)

# 嵌套拆包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
]
print('{:15} | {:^9} | {:^9}'.format('city.', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0 : print(fmt.format(name, latitude, longitude))

## named tuples
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # City(*delhi_data)
tDict = delhi._asdict() #OrderedDict
for key, value in tDict.items(): print(key+':', value)