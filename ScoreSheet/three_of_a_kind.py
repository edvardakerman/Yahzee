class Three_of_a_kind:
    score = 0
    taken = False
    type = 7
    name = "Three of a kind"

    def calcScore(self, dice):
        dice = sorted(dice, key=lambda x: x.value, reverse=True)
        if dice[0].value == dice[1].value == dice[2].value:
            self.score = dice[0].value + dice[1].value + dice[2].value
        elif dice[2].value == dice[2].value == dice[4].value:
            self.score = dice[2].value + dice[3].value + dice[4].value