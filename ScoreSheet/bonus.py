from ScoreSheet.basic import Basic
from colors import Colors

class Bonus(Basic):
    countBase = 0
    baseScore = 0

    def calcBonus(self, dice_value):
        self.baseScore += dice_value
        self.countBase += 1
        if self.baseScore >= 63:
            self.score = 50
            self.taken = True
        elif self.countBase == 6:
            self.taken = True
        else:
            self.score = 0
        self.statusColor()