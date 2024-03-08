class Chance:
    score = 0
    taken = False
    type = 13
    name = "Chance        "

    def sumAll(self, dice):
        sum = 0
        for die in dice:
            sum += die.value
        return sum

    def calcScore(self, dice):
        self.score = self.sumAll(dice)