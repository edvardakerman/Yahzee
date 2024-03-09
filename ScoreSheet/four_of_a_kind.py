from ScoreSheet.basic import Basic

class Four_of_a_kind(Basic):

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        if dice[0].value == dice[1].value == dice[2].value == dice[3].value:
            self.score = dice[0].value + dice[1].value + dice[2].value + dice[3].value
        elif dice[1].value == dice[2].value == dice[2].value == dice[4].value:
            self.score = dice[1].value + dice[2].value + dice[3].value + dice[4].value
        self.statusColor()