import zombiedice,random

class MyZombie:
    isContinue =True
    def __init__(self,name):
        #All zombies most have name:
        self.name = name
    def turn(self,gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2  and self.isContinue:
                diceRollResults = zombiedice.roll()
                if random.randint(0,1):
                    self.isContinue = False
            else:
                break 

zombies =  (zombiedice.examples.RandomCoinFlipZombie(name='random'),
            zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'stop at 2 Shotguns',minShotguns=2),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'stop at 1 Shotgun',minShotguns=1),
            MyZombie(name = 'My zombie Bot'),
            )
zombiedice.runWebGui(zombies=zombies,numGames=1000)
