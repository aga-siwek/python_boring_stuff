#try, except in def


def spam(divide_by):
    try: 
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0)) # error
print(spam(1))


#try, except in fonction

def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0)) # error
    print(spam(1))

except ZeroDivisionError:
    print("Error: Invalid argument.")