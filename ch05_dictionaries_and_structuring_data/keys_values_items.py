spam = {"color" : "red", "age" : 42}
for v  in spam.values():
    print (v) #print values not key

for k in spam:   
    print(k) #print key

for ke in spam.keys():
    print(ke) #the same like before, pront keys

for i in spam.items():
    print(i) #print truple items with key and value

print("red" in spam.values())
print("blue" in spam.values())
print("color" in spam.values())
print("color" in spam.keys())
print("color" in spam) # the same like previous
print("color" not in spam.values())
print("color" not in spam.keys())