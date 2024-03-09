
from ScoreSheet.straight import Straight
from player import Player
from dice import Dice

def getSpace(name):
    return "1" * (16 - len(name))

print("Test of print: " + getSpace("test"))