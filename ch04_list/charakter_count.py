message = " it was a bringht cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
    count.setdefault(character,0)
    count[character]= count[character] +1

print(count)




message = "pa pa pa this is song in my heart la la la la la"
song = {}
for character in message:
    song.setdefault(character,0)
    song[character] = song[character] + 1
print(song)