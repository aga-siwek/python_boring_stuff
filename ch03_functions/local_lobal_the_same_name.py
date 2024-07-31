
def spam():
    eggs = "spam local"
    print(eggs) #print "spam local"

def bacon():
    eggs = "bacon local"#prints "bacon eggs"
    print(eggs)
    spam()
    print(eggs) #prints bacon eggs

eggs = "global"
bacon()
print(eggs) #prints global
