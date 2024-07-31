if __name__ == '__main__':
    import pyinputplus as pyip

    bread = pyip.inputMenu(["wheat", "withe", "sourdough"], prompt = "Choose a bread type: \n")
    protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt = "Choose a protein type: \n")
    cheese_YN = pyip.inputYesNo("Do you want cheese?: ", yesVal="yes", noVal="no")
    if cheese_YN == "yes":
        cheese = pyip.inputMenu(["cheddar", "Swiss", "Mozzarella"], prompt="Choose a cheese type: \n")
    additives = pyip.inputYesNo("Do you want mayo, mustard, lettuce or tomato?: ", yesVal="yes", noVal="no")
    sandwiches_num = pyip.inputInt("How many sandiches do you want?")


    print (f"samdwich {sandwiches_num}, with {protein}, {cheese}, {additives}")

