class InputHandling:
    
    def getInt(min, max):
        num = int
        while True:
            try:
                num = int(input())
                if num < min or num > max:
                    print("Invalid input. Please enter a number between " + str(min) + " and " + str(max))
                else:
                    return num
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def getSavedDice():
        dice = str
        num = []
        while True:
            dice = str(input())
            for i in range(len(dice)):
                try:
                    num.append(int(dice[i]))
                except ValueError:
                    print("Invalid input. Please enter only valid number(s).")
            if len(num) == len(dice):
                return num
    
    