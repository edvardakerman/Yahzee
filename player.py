from ScoreSheet.basic import Basic
from ScoreSheet.bonus import Bonus
from ScoreSheet.chance import Chance
from ScoreSheet.full_house import Full_house
from ScoreSheet.straight import Straight
from ScoreSheet.of_a_kind import Of_a_kind
from ScoreSheet.two_pairs import Two_pair
from colors import Colors

class Player:

    def __init__(self, name, color):
        self.score = 0
        self.name = name
        self.color = color
        self.ones = Basic(1, "Ones", color)
        self.twos = Basic(2, "Twos", color)
        self.threes = Basic(3, "Threes", color)
        self.fours = Basic(4, "Fours", color)
        self.fives = Basic(5, "Fives", color)
        self.sixes = Basic(6, "Sixes", color)
        self.pair = Of_a_kind(7, "Pair", color, 2)
        self.two_pair = Two_pair(8, "Two pairs", color)
        self.three_of_a_kind = Of_a_kind(9, "Three of a kind", color, 3)
        self.four_of_a_kind = Of_a_kind(10, "Four of a kind", color, 4)
        self.full_house = Full_house(11, "Full house", color)
        self.sm_straight = Straight(12, "Small straight", color)
        self.lg_straight = Straight(13, "Large straight", color)
        self.yahzee = Of_a_kind(14, "YAHZEE", color, 5)
        self.chance = Chance(15, "Chance", color)
        self.bonus = Bonus(16, "Bonus", color)
        self.base = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.pair, self.two_pair, self.three_of_a_kind, self.four_of_a_kind, self.full_house, self.sm_straight, self.lg_straight, self.yahzee, self.chance]
    
    def setName(self, name):
        self.name = name


    def takeScore(self, type, dice):
        for i in self.base:
            if i.type == type and not i.taken:
                i.taken = True
                i.calcScore(dice)
                self.score += i.score
                if i.type in range(1, 7) and self.bonus.taken == False:
                    self.bonus.calcBonus(i.score)
                    self.score += self.bonus.score
                return True
        return False

    def showSS(self):
        print("Score sheet for " + self.name + ":")
        print("-----------------------------")
        for i in self.base:
            i.print()
        Bonus.print(self.bonus)
        print(Colors.BOLD + "| Total: " + str(self.score) + Colors.ENDC)
        print("-----------------------------") 