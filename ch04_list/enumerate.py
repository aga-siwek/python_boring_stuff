supplies = ["pens", "staplers", "flamethrowers", "binders"]
for index, item in enumerate(supplies):
    print("index " + str(index) + " in supplies is: " + item)


answers = ["answer 1", "answer 2", "answer 3", "answer 4"]
import random
random.shuffle(answers)
print(answers[0])