cat_name = []
while True:
    name = input("Enter the name of cat " + str(len(cat_name)+1) + ("(or enter nothing to stop).: "))
    if name == "":
        break
    cat_name = cat_name + [name] #list coonection 
print("The cat name are: ", end=": ")
for name in cat_name: 
    print(name, end=", ")
