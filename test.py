
from ScoreSheet.straight import Straight
from ScoreSheet.two_pairs import Two_pair
from Yahzee.ScoreSheet.of_a_kind import Three_of_a_kind
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
dice[1].value = 5
dice[2].value = 5
dice[3].value = 5
dice[4].value = 5

## Player

three_of_a_kind = Three_of_a_kind(9, "Three of a kind", Colors.BLUE, 3)
four_of_a_kind = Three_of_a_kind(9, "Three of a kind", Colors.BLUE, 4)
pair = Three_of_a_kind(9, "Three of a kind", Colors.BLUE, 2)
y = Three_of_a_kind(9, "Three of a kind", Colors.BLUE, 5)

three_of_a_kind.calcScore(dice)
four_of_a_kind.calcScore(dice)
pair.calcScore(dice)
y.calcScore(dice)

print("Pair: " + str(pair.score))
print("Three of a kind: " + str(three_of_a_kind.score))
print("Four of a kind: " + str(four_of_a_kind.score))
print("Yahzee: " + str(y.score))