import keyword

# float
a = 1 + 2.55

print(a)

# None
n = None

print(n)

# Keyword list
print(keyword.iskeyword("a"))
print(keyword.iskeyword("try"))
print(keyword.kwlist)

# id of object
print(id(a))

# list
b = [1, 2]
print(b)
b[0] = 3
print(b)

# type of b
print(type(b))

# tuple
c = ("a", "b")
print(c)
print(type(c))

# dict
d = {1: 'Abc', 'E': 12345}
print(d)
print(type(d))
