class Yahzee:
    score = 0
    taken = False
    type = 12
    name = "YAHZEE!       "

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        if dice[0].value == dice[4].value:
            self.score = 50