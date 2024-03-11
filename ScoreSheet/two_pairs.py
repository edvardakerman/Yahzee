from ScoreSheet.basic import Basic

class Two_pair(Basic):

    def calcScore(self, dice):
        pairOne = 0
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        prevVal = dice[0].value
        for d in range(1, 5):
            if dice[d].value == prevVal:
                if pairOne == 0:
                    pairOne = prevVal * 2
                elif dice[d].value != (pairOne / 2):
                    self.score = prevVal * 2 + pairOne
                    break
            prevVal = dice[d].value
        self.statusColor()