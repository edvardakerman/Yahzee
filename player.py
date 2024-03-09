from ScoreSheet.basic import Basic
from ScoreSheet.bonus import Bonus
from ScoreSheet.chance import Chance
from ScoreSheet.four_of_a_kind import Four_of_a_kind
from ScoreSheet.full_house import Full_house
from ScoreSheet.straight import Straight
from ScoreSheet.three_of_a_kind import Three_of_a_kind
from ScoreSheet.yahzee import Yahzee
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
        self.three_of_a_kind = Three_of_a_kind(7, "Three of a kind", color)
        self.four_of_a_kind = Four_of_a_kind(8, "Four of a kind", color)
        self.full_house = Full_house(9, "Full house", color)
        self.sm_straight = Straight(10, "Small straight", color)
        self.lg_straight = Straight(11, "Large straight", color)
        self.yahzee = Yahzee(12, "Yahzee", color)
        self.chance = Chance(13, "Chance", color)
        self.bonus = Bonus(14, "Bonus", color)
        self.base = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.three_of_a_kind, self.four_of_a_kind, self.full_house, self.sm_straight, self.lg_straight, self.yahzee, self.chance]
    
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