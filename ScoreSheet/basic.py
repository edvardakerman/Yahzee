from colors import Colors

class Basic:
    printNrChar = 15

    def __init__(self, type, name, color):
        self.type = type
        self.name = name
        self.score = 0
        self.taken = False
        self.status = color
    
    def getSpace(self):
        return " " * (Basic.printNrChar - len(self.name))
    
    def getSpaceInt(num):
        if num < 10:
            return " "
        else:
            return ""
    
    def statusColor(self):
        if self.taken == True:
            if self.score == 0:
                self.status = Colors.RED
            else:
                self.status = Colors.GREEN

    def calcScore(self, dice):
        for d in dice:
            if d.value == self.type:
                self.score += self.type
        self.statusColor()

    def print(self):
        print(self.status + "| " + str(self.type) + Basic.getSpaceInt(self.type) +" | " + self.name + self.getSpace() + " | " + str(self.score) + Basic.getSpaceInt(self.score) + " |" + Colors.ENDC)
        print("-----------------------------")

    