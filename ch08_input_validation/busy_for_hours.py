import pyinputplus as pyip


if __name__ == '__main__':
    while True:
        response = pyip.inputYesNo("Want to know how to keep an a idiot busy for hours? ", yesVal = "yes", noVal = "no" )
        if response == "no":
            print("ok your choose")
            break
