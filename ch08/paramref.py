def f(a,b):
    a += b
    return a
x = 1; y = 2; print('x','y'); print(x,y); f(x,y); print(x,y)
a = [1,2]; b = [3,4]; print('a','b'); print(a,b); f(a,b); print(a,b)
t = (10, 20); u = (30,40); print('t','u'); print(t,u); f(t,u); print(t,u)

##########################################
# demo with empty list as function parameter
class HauntedBus:
    ''' A bus model haunted by ghost passengers '''

    def __init__(self, passengers=[]):
        self.passengers = passengers # can use list(passengers) to get a different ref

    def pick(self, name):
        self.passengers.append(name)
        return self.passengers

    def drop(self, name):
        self.passengers.remove(name)
        return self.passengers

bus1 = HauntedBus(['Alice', 'Bill'])
print('bus1:', bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print('bus1:', bus1.passengers)
bus2 = HauntedBus()
print('bus2 with default empty passenger list')
print('bus2:', bus2.pick('Carrie'))
bus3 = HauntedBus()
print('bus3 with default empty passenger list')
print('bus3:', bus3.pick('Dave'))
print('bus2:', bus2.passengers)
print('bus2.passengers is bus3.passengers: ', bus2.passengers is bus3.passengers)
print('bus1:', bus1.passengers)
# all HauntedBus instances share the same empty list instance
print(HauntedBus.__init__.__defaults__[0] is HauntedBus().passengers)

# empty list ids
print(id([]), id([]))
xx = []; yy = []
print(id([]), id(xx), id(yy))