l1 = []
print(type(l1))

l2 = [1, 2, 'ABC', 1234]
print(type(l2))

l3 = list()
print(type(l3))

l3.append(1)
l3.append(10)
print(l3)

l3.remove(10)
print(l3)

del l3[0]
print(l3)
