import time, sys

insert = 0
loop_zigzag = True

try:
    while True:

        print(" " * insert, end="")
        print("********")
        time.sleep(0.1)
        if loop_zigzag == True:
            insert += 1
            if insert == 2:
                loop_zigzag = False
        else:
            insert -= 1
            if insert == 0:
                loop_zigzag = True
except KeyboardInterrupt:
    sys.exit
