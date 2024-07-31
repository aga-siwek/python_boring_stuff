a = 10
a = 11
b = 12.5
a = b
b = 10

print(type(a))
print(a)

print(type(b))
print(b)

c = a + b

print(type(c))
print(c)

b = 15
c = a + b
print(c)