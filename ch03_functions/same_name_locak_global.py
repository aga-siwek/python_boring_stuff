def spam():
   global eggs
   eggs = "spam" #this is the global

def bacon():
    eggs = "bacon" #this is a local

def ham():
    print("ham start")
    print(eggs) #this is the global
    print("ham stop")

eggs = 42 #this is a global

print(eggs)
ham()
spam()
print(eggs)
ham()
