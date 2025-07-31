"""
Develop a program that simulates rolling a six-sided dice. When run, the program should generate and display a random number between 1 and 6, representing the dice roll.
"""

import random

# dice = random.randint(1,6)
# print (f"the number is - ",dice)


def roll_dice():
    return random.randint(1,6)

print("Rolling the dice...")
print(f"The number is: {roll_dice()}")