
from ScoreSheet.straight import Straight
from player import Player
from dice import Dice

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice = [dice1, dice2, dice3, dice4, dice5]
playerOne = Player("one")

for n in range(3, 7):
    print("Testing " + str(n) + "...")
    dice[0].value = n
    dice[1].value = n
    dice[2].value = n
    dice[3].value = n
    dice[4].value = 1
    playerOne.takeScore(n, dice)

playerOne.showSS()
