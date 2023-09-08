import random

class Dice:

    def roll(self):
        x = random.randint(0,6)
        y = random.randint(0,6)
        # r = ( x, y )
        return x, y
dice = Dice()
print(dice.roll()) 