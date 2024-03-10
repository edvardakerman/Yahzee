
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
            except KeyboardInterrupt:
                print("\nExiting..")
                exit(0)
    
    def getSavedDice():
        dice = str
        num = []
        while True:
            dice = InputHandling.getString()
            for i in range(len(dice)):
                try:
                    num.append(int(dice[i]))
                except ValueError:
                    print("Invalid input. Please enter only valid number(s).")
            if len(num) == len(dice):
                return num
    
    def getString():
            try:
                return str(input())
            except KeyboardInterrupt:
                print("\nExiting..")
                exit(0)

        