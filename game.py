from highScore import HighScore
from inputHandling import InputHandling
from colors import Colors
from dice import Dice
from player import Player

## Dice
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice = [dice1, dice2, dice3, dice4, dice5]

## Players
playerOne = Player("one", Colors.CYAN)
playerTwo = Player("two", Colors.PINK)
playerThree = Player("three", Colors.YELLOW)
playerFour = Player("four", Colors.BLUE)
players = [playerOne, playerTwo, playerThree, playerFour]

## Turns
turns = 0

## Functions
def roll_dice(dice):
    print("Rolling dice...")
    dice = sorted(dice, key=lambda x: x.keep, reverse=True)
    for i in dice:
            if i.keep:
                print("Saved dice: " + str(i.value))
            else:
                i.roll()
                print("New dice: " + str(i.value))

def keep_dice(saved_dice):
    for i in saved_dice:
        for d in dice:
            if d.value == i and d.keep == False:
                d.save(True)
                break

def player_Choice(dice, throw):
        for k in dice:
            k.save(False)
        if throw <= 1:
            print("\nWhich dice do you want to keep?")
            saved_dice = InputHandling.getSavedDice()
            keep_dice(saved_dice)
        
def score_Choice(player):
    print("\nPlease choose from you score sheet (1-15)")
    scoreChoice = InputHandling.getInt(1, 15)
    while not player.takeScore(scoreChoice, dice):
        print("Invalid choice. Please choose a valid number that has not been taken from your Score Sheet.")
        scoreChoice = InputHandling.getInt(1, 15)
    for i in dice:
        i.save(False)

## Game
print(Colors.HEADER + "\nWelcome to Yahtzee!" + " Try to set a new highscore!!" + Colors.ENDC)
if (HighScore.getHighScore() > 0):
    print("The current highscore is " + str(HighScore.getHighScore()))
print("\nHow many players are there? (1-4)")
numPlayers = InputHandling.getInt(1, 4)
players = players[:numPlayers]
for i in range(len(players)):
    print("\nEnter player " + str(i + 1) + "'s name:")
    name = InputHandling.getString()
    players[i].setName(name)

print("\nLet's play!")

for t in range(15):
    print("\nRound " + str(t+1) + " / 15")
    for player in players:
        print('\n' + player.name + ", it's your turn!")
        player.showSS()
        for n in range(3):
            print("\nThrow " + str(n+1))
            roll_dice(dice)
            player_Choice(dice, n)
        score_Choice(player)
        player.showSS()
    

print("\nGame over!")
players.sort(key=lambda x: x.score, reverse=False)
print(Colors.BOLD + "The winner is... " + players[0].name + "!!\n" + Colors.ENDC)
HighScore.saveHighScore(players[0].score)

for p in range(len(players)):
    print(str(p + 1) + ". " + players[p].name + ", your final score is: " + str(players[p].score))
    
if (HighScore.getHighScore() < players[0].score):
    print("\nYou set a new Highscore!!!" + str(HighScore.getHighScore()))
    print("The old highscore was " + str(HighScore.getHighScore()) + ", the new highscore is " + str(players[0].score) + "!!")
    print("Congratulations " + players[0].name + "!!")
else:
    print("\nYou did not set a new highscore. The highscore is still " + str(HighScore.getHighScore()) + ".")
    print("Better luck next time!")



