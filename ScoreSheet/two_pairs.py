from ScoreSheet.basic import Basic

class Two_pair(Basic):

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)        
        if dice[0].value == dice[3].value or dice[1].value == dice[4].value:
            self.score = dice[0].value * 4
        else:
            pairOne = 0
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