class HighScore:
    fileName = "highscore.txt"

    def saveHighScore(newScore):
        if (newScore > HighScore.getHighScore()):
            f = open(HighScore.fileName, "w")
            f.write(str(newScore))
            f.close
        
        
    def getHighScore():
        highScore = int
        try:
            f = open(HighScore.fileName, "r")
            highScore = f.readline()
            f.close()
            try:
                return int(highScore)
            except ValueError:
                return 0
        except FileNotFoundError:
            return 0



    