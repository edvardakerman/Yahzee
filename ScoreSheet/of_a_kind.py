from ScoreSheet.basic import Basic

class Of_a_kind(Basic):
    count = 0
    
    def __init__(self, type, name, color, kind):
        self.kind = kind
        super().__init__(type, name, color)

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        prevVal = dice[0].value
        for d in range(1, 5):
            if self.count == (self.kind -1) or (self.count == (self.kind -2) and dice[d].value == prevVal):
                self.score = prevVal * self.kind
                break
            if dice[d].value == prevVal:
                self.count += 1
            else :
                self.count = 0
            prevVal = dice[d].value
        self.statusColor()
        