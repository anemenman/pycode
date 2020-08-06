t = (1, 2, 3)
print(t)
print(type(t))

# TypeError: 'tuple' object does not support item assignment
# t[0] = 1

l = list(t)
print(l)

t2 = tuple(l)
print(t2)
