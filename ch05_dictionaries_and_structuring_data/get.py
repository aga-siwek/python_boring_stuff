picnic_items = {"apples": 5, "cups": 2}
print(" I am bring " + str(picnic_items.get("eggs", 0))+" eggs")
print(picnic_items)


#get metod, if the key doesn't exist in dictionary, for this key we get a value for keys, and value 
things_to_get = input("write what miss: ")
print(" I am bring " + str(picnic_items.get(things_to_get, 0))+" " + str(things_to_get))
print(type(picnic_items))


#setdefault()

