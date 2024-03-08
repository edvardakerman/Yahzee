
from ScoreSheet.straight import Straight
from dice import Dice

sm_straight = Straight(10, "Small straight")
lg_straight = Straight(11, "Large straight")

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice = [dice1, dice2, dice3, dice4, dice5]

# dice[0].value = 5
# dice[1].value = 2
# dice[2].value = 3
# dice[3].value = 4
# dice[4].value = 1

dice[0].value = 4
dice[1].value = 3
dice[2].value = 2
dice[3].value = 3
dice[4].value = 6
          
##sm_straight.calcScore(dice)
lg_straight.calcScore(dice)

##print("Small straight: " + str(sm_straight.score))
print("Large straight: " + str(lg_straight.score))

print("Sorted:")
for i in dice:
    print(i.value)