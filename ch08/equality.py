###################################
# Equality
charles = {'name':'Charles L. Dodgon', 'born':1832}
lewis = charles
print(lewis is charles) # True
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)
alex = {'name':'Charles L. Dodgon', 'born':1832, 'balance':950}
print(alex == charles) # True
print(alex is not charles) # True

#################################
# tuple immutability
t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(t1 == t2) # True
t1[-1].append(99)
print(t1)
print(t1 == t2) # False