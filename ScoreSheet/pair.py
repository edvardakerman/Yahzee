from ScoreSheet.basic import Basic

class Pair(Basic):

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        prevVal = dice[0].value
        for d in range(1, 5):
            if dice[d].value == prevVal:
                self.score = dice[d].value * 2
                break
            prevVal = dice[d].value
        self.statusColor()