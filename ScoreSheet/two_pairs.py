from ScoreSheet.basic import Basic

class Two_pair(Basic):

    def calcScore(self, dice):
        pairOne = 0
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        prevVal = dice[0].value
        for d in range(1, 5):
            if dice[d].value == prevVal:
                print("Dice: " + str(d) + "Val: " + str(dice[d].value) + "PrevVal: " + str(prevVal))
                if pairOne == 0:
                    print("yeah")
                    pairOne = prevVal * 2
                elif dice[d].value != (pairOne / 2):
                    print("YEAH")
                    self.score = prevVal * 2 + pairOne
                    break
            prevVal = dice[d].value
        self.statusColor()
        print("Score: " + str(self.score))