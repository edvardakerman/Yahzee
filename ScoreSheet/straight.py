class Straight:
    score = 0
    taken = False
    count = 0
    prevVal = 0

    def __init__(self, type, name):
        self.name = name
        self.type = type

    def calcScore(self, dice):
        ##dice = sorted(dice, key=lambda x: x.value, reverse=False)
        dice.sort(key=lambda x: x.value, reverse=False)
        self.prevVal = dice[0].value
        for d in range(1, 5):

            if dice[d].value == self.prevVal + 1:
                ##print("Dice val: " + str(dice[d].value) + " Prev dice val: " + str(self.prevVal + 1))
                self.count += 1
                self.prevVal = dice[d].value
        if self.count == 4:
            ##print("Last: " + str(dice[4].value))
            if dice[4].value == 5:
                self.score = 15
            elif dice[4].value == 6:
                self.score = 20
        self.count = 0