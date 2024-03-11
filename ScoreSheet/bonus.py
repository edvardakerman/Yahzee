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
    
    def calcBaseScore(self, base):
        baseScore = 0
        for b in base:
            baseScore += b.score
        return baseScore
    
    def print(self, base):
        baseScore = self.calcBaseScore(base)
        print(self.status + "| " + str(self.type) + Basic.getSpaceInt(self.type) +" | " + self.name + " (" + str(baseScore) + ")" + Basic.getSpaceInt(baseScore) + "      | " + str(self.score) + Basic.getSpaceInt(self.score) + " |" + Colors.ENDC)
        print("-----------------------------")