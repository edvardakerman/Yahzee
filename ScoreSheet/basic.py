class Basic:
    score = 0
    taken = False

    def __init__(self, type, name):
        self.type = type
        self.name = name

    def calcScore(self, dice):
        for d in dice:
            if d.value == self.type:
                self.score += self.type

    