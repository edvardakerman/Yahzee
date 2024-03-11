
from ScoreSheet.straight import Straight
from ScoreSheet.two_pairs import Two_pair
from colors import Colors
from player import Player
from dice import Dice

## Dice
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice = [dice1, dice2, dice3, dice4, dice5]

dice[0].value = 5
dice[1].value = 3
dice[2].value = 3
dice[3].value = 4
dice[4].value = 4

## Player
two_pair = Two_pair(8, "Two pairs", Colors.CYAN)

two_pair.calcScore(dice)

print("Two Pair: " + str(two_pair.score))