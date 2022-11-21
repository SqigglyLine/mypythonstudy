import random


class Dice:

    def roll(self):
        dice_numbers = (1, 2, 3, 4, 5, 6)
        rolled = random.choice(dice_numbers)
        rolled2 = random.choice(dice_numbers)
        print(f'{rolled}, {rolled2}')


roll = Dice()
roll.roll()
