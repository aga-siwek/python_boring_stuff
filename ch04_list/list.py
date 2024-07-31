spam = ["cat", "bat", "rat", "elephant"]
print(len(spam[1]))
spam[1] = "aardvark"
print(spam)
print(len(spam[1]))

spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)