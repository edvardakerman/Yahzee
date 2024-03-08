from colors import Colors

class Bonus:
    score = 0
    taken = False
    type = 14
    name = "Bonus"
    totScore = 0
    countBase = 0

    def calcScore(self, base):
        for b in range(0, 5):
            self.totScore += base[b].score
            if base[b].taken:
                self.countBase += 1
        if self.totScore >= 63:
            self.score = 50
            self.taken = True
        elif self.countBase == 6:
            self.taken = True
        else:
            self.totScore = 0

    def print(self):
        if self.taken:
            print(Colors.OKGREEN + "| Bonus               | " + str(self.score) + " |" + Colors.ENDC)
        else:
            print(Colors.OKBLUE + "| Bonus               | X |" + Colors.ENDC)