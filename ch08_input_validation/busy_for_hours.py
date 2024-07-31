import pyinputplus as pyip

while True:
    response = pyip.inputYesNo("Want to know how to keep an a idiot busy for hours? ", yesVal = "yes", noVal = "no" )
    if response == "no":
        print("ok your choose")
        break
