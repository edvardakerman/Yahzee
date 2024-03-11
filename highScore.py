class HighScore:
    
    def __init__(self):
        self.fileName = "highscore.txt"
        self.score = int
        self.name = ""
        self.getHighScore()

    def saveHighScore(self, newScore, newName):
        if (int(newScore) > int(self.score)):
            f = open(self.fileName, "w")
            f.write(newName + ", " + str(newScore))
            f.close
    
    def getHighScore(self):
        try:
            f = open(self.fileName, "r")
            info = f.readline().split(", ")
            self.name = info[0]
            self.score = info[1]
            f.close()
        except FileNotFoundError or ValueError:
            self.score = 0
            self.name = ""



    