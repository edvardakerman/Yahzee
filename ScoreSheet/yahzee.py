from ScoreSheet.basic import Basic

class Yahzee(Basic):

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        if dice[0].value == dice[4].value:
            self.score = 50
        self.statusColor()