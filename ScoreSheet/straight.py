from ScoreSheet.basic import Basic

class Straight(Basic):
    count = 0
    prevVal = 0

    def calcScore(self, dice):
        dice.sort(key=lambda x: x.value, reverse=False)
        self.prevVal = dice[0].value
        for d in range(1, 5):
            if dice[d].value == self.prevVal + 1:
                self.count += 1
                self.prevVal = dice[d].value
        if self.count == 4:
            if dice[4].value == 5:
                self.score = 15
            elif dice[4].value == 6:
                self.score = 20
        self.count = 0
        self.statusColor()