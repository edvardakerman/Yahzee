from ScoreSheet.basic import Basic

class Chance(Basic):

    def sumAll(self, dice):
        sum = 0
        for die in dice:
            sum += die.value
        return sum

    def calcScore(self, dice):
        self.score = self.sumAll(dice)
        self.statusColor()