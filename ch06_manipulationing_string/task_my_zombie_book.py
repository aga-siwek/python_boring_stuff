import zombiedice

class my_zombie:
    def __init__(self, name):
        #all zombies must have a name:
        self.name = name

    def turn(self, game_state):
        #game_state is a dict with info abaut the current state of the game
        #you can choose to ignore it in a code. 
        dice_roll_results = zombiedice.roll() #first roll


        #replace this zombie code with your own

        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results["brains"]

            if brains < 2:
                dice_roll_results = zombiedice.roll() #roll again
            else: 
                break


class zombie_bot_decided:
    
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        import random
        brains = 0
        dice_roll_result = zombiedice.roll()

        while True:
            if dice_roll_result == None:
                brains = 0
                break
            decision = random.choice(["Yes", "No"])
            if decision == "No":
                brains += dice_roll_result["brains"]
                break
            brains += dice_roll_result["brains"]
            dice_roll_result = zombiedice.roll()


class zombie_2_shotguns_stop:

    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        brains = 0
        dice_roll_result = zombiedice.roll()

        while True:
            if dice_roll_result == None:
                brains = 0
                break
            if dice_roll_result["footsteps"] == 2 and dice_roll_result["brains"] == 1:
                brains += dice_roll_result["brains"]
                break 
            brains += dice_roll_result["brains"]
            dice_roll_result = zombiedice.roll()


class Zombie_random_1_4:
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        import random
        brains = 0
        dice_roll_result = zombiedice.roll()
        num_roll = random.randrange(1,4)

        for i in range(num_roll):
            if dice_roll_result == None:
                return
            brains += dice_roll_result["brains"]
            dice_roll_result = zombiedice.roll()


class brain_vs_shotgun:
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        brains = 0 
        dice_roll_result = zombiedice.roll()
        while True:
            if dice_roll_result == None:
                brains = 0
                break
            if dice_roll_result["shotgun"] > dice_roll_result["brains"]:
                brains += dice_roll_result["brains"]
                break
            brains += dice_roll_result["brains"]
            dice_roll_result = zombiedice.roll()


            
class Zombie_test:
    """This bot keeps rolling until it has rolled a minimum number of shotguns, then it rolls one more time."""
    def __init__(self, name):
        self.name = name
  

    def turn(self, gameState):
        shotguns = 0 # number of shotguns rolled this turn
        while shotguns < 2:
            diceRollResults = zombiedice.roll()

            if diceRollResults is None:
                return

            shotguns += diceRollResults["shotgun"] # increase shotguns by the number of shotgun die rolls.
        diceRollResults = zombiedice.roll() # Roll one more time.

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name = "Random"),
    zombiedice.examples.MonteCarloZombie(name = "Monte Carlo", riskiness = 40, numExperiments = 20),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = "Stop at the 2 shotguns", minShotguns = 2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = "Stop at the 1 shotgun", minShotguns = 1),
    zombiedice.examples.RollsUntilInTheLeadZombie(name = "Until leading"), my_zombie(name = "My zombie bot"), zombie_bot_decided(name = "zombie bot decided"), zombie_2_shotguns_stop(name = "zombie after 2 shotguns stop"),Zombie_test(name="copy form"), Zombie_random_1_4(name = "random roll 1-4"), brain_vs_shotgun(name = "brain vs shotgun")
)

        # #roll() returns a dictionary with keys "brains, "shotgun, and footsteps with how many rols ot the type there were.
        # #the rolls key is a list of (color, icon) tru#example of roll() r
        # # {"brains": 1, "footsteps": 1, "shotgun": 1, "rolls":[("yellow", "brains"), (red":"footsteps"), ("green", "shotgun")]}

        # #replace thi

        # name = my_zombie("Pawel")
        # print(name.turn())

zombiedice.runWebGui(zombies=zombies, numGames=1000)
