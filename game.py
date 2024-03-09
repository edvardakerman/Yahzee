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
            print("Which dice do you want to keep?")
            saved_dice = [int(i) for i in str(input())]
            keep_dice(saved_dice)
        
def score_Choice(player):
    print("Please choose from you score sheet (1-13)")
    scoreChoice = int(input())
    while not player.takeScore(scoreChoice, dice):
        print("Invalid choice. Please choose a valid number that has not been taken.")
        scoreChoice = int(input())
    for i in dice:
        i.save(False)

## Game
print("Welcome to Yahtzee!")
print("How many players are there? (1-4)")
numPlayers = int(input())
players = players[:numPlayers]
for i in range(len(players)):
    print("Enter player " + str(i + 1) + "'s name:")
    name = str(input())
    players[i].setName(name)

print("Let's play!")

for t in range(15):
    print("Round " + str(t+1) + " / 15") 
    for player in players:
        print(player.name + ", it's your turn!")
        player.showSS()
        for n in range(3):
            print("Throw " + str(n+1))
            roll_dice(dice)
            player_Choice(dice, n)
        score_Choice(player)
        player.showSS()
    

print("Game over!")
players.sort(key=lambda x: x.score, reverse=False)
print(Colors.BOLD + "The winner is... " + players[0].name + "!!" + Colors.ENDC)

for p in range(len(players)):
    print(str(p + 1) + ". " + players[p].name + ", your final score is: " + str(players[p].score))

