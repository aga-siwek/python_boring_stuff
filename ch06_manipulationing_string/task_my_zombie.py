import zombiedice

class my_zombie:
    def __init__(self, name):
        #all zombies must have a name:
        self.name = name

    def turn(self, game_state):
        #game_state is a dict with info abaut the current state of the game
        #you can choose to ignore it in a code. 
        shotguns_rolled = 0
        while shotguns_rolled <2:
            results = roll()

        if results == []:
            # zombie has reached 3 or more shotguns.
            return
        
        for i in results:
            #count shotguns in results.
            if i[ICON] == SHOTGUN:
                shotguns += 1

zombices = (
    zombiedice.examples.RandomCoinFlipZombie(name = "Random"),
    zombiedice.examples.MonteCarloZombie(name = "Monte Carlo", riskiness = 40, numExperiments = 20),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = "Min 2 shutguns", minShotguns = 2)
    #add any other zombie playes here
    )

zombiedice.runWebGui(zombies=zombices, numGames=1000)

        # dice_roll_results = zombiedice.roll() #first roll
        # #roll() returns a dictionary with keys "brains, "shotgun, and footsteps with how many rols ot the type there were.
        # #the rolls key is a list of (color, icon) tru#example of roll() r
        # # {"brains": 1, "footsteps": 1, "shotgun": 1, "rolls":[("yellow", "brains"), (red":"footsteps"), ("green", "shotgun")]}

        # #replace thi

        # name = my_zombie("Pawel")
        # print(name.turn())

