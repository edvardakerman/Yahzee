class Full_house:
    score = 0
    taken = False
    type = 9
    name = "Full house     "

    def sumAll(self, dice):
        sum = 0
        for die in dice:
            sum += die.value
        return sum


    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        if dice[0].value == dice[2].value and dice[3].value == dice[4].value:
            self.score = self.sumAll(dice)
        elif dice[0].value == dice[1].value and dice[2].value == dice[4].value:
            self.score = self.sumAll(dice)