import random

class Dice:
    value = int
    keep = False

    def roll(self):
        if not self.keep:
            self.value = random.randint(1, 6)
    
    def print(self):
        print(self.value)

    def save(self, bool):
        self.keep = bool