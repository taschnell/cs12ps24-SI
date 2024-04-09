"""
Solution for the week five weekly practice -- A program that roles two dice
"""
import random

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
"""
random.randint(a, b)

    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

"""

# Dice 1
if dice_1 == 1:
    print("\u2680")
elif dice_1 == 2:
    print("\u2681")
if dice_1 == 3:
    print("\u2682")
if dice_1 == 4:
    print("\u2683")
if dice_1 == 5:
    print("\u2684")
if dice_1 == 6:
    print("\u2685")    

# Dice 2
if dice_2 == 1:
    print("\u2680")
if dice_2 == 2:
    print("\u2681")
if dice_2 == 3:
    print("\u2682")
if dice_2 == 4:
    print("\u2683")
if dice_2 == 5:
    print("\u2684")
if dice_2 == 6:
    print("\u2685")    