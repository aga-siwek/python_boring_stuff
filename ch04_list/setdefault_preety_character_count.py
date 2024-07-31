import pprint
message = "it was a bringht cold day in April, and the clocks were striking thirteen."

count ={}

for charakter in message.lower():
    count.setdefault(charakter, 0)
    count[charakter] += 1
pprint.pprint(count)
print(pprint.pformat(count))