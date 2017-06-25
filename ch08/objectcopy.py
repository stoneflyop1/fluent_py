##################################
# shallow copy demo with list
l1 = [3,[66,55,44], (7,8,9)]
l2 = list(l1)
l3 = l1[:]
print(l2 == l1) # have same referenced values
print(l3 == l1) # have same referenced values
print(l2 is l1) # not same ids
print(l3 is l1) # not same ids

#####################################
# shallow copy with mutable objects
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33,22] # += on list means extend
l2[2] += (10,11) # += on tuple means extend and return a new tuple
print('l1:', l1)
print('l2:', l2)


######################################
# shallow and deep copy
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)
        return self.passengers

    def drop(self, name):
        self.passengers.remove(name)
        return self.passengers

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
print('bus1:', bus1.drop('Bill'))
print('bus2:', bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print('bus3:', bus3.passengers)

###########################
# deepcopy with cyclic references
a = [10,20]
b = [a, 30]
a.append(b)
print(a)
c = copy.deepcopy(a)
print(c)