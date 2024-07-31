# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)

spam = [0, 1, 2, 3, 4]
cheese = spam
cheese[1] = "hello"
print(spam)
print(id(spam))