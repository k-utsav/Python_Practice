"""
Write a simple "Guess the Number" game.
The program should "think" of a random number between 1 and 10 (inclusive).
Then, it should ask the user to guess the number.
If the guess is correct, print "Congratulations! You guessed it!".
If the guess is too high, print "Too high! Try again.".
If the guess is too low, print "Too low! Try again.".
The game should allow the user to keep guessing until they get it right.
"""

import random

secret_num = random.randint(1,10)
# print (secret_num)
print("I am thinking of a number between 1 and 10")

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == secret_num:
        print(f"Congratulation!! You gueesed it right. The number is: ",secret_num)
        break
    
    elif user_guess < secret_num:
        print("Too Low, Try again")
    else:
        print("Too High, Try again")
        