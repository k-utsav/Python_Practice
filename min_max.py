# take input from user about the quantity of number

import random

num_range = int(input("Enter the number of random numbers to generate: "))

minimum_range = int(input("Enter a number for mimimum range: "))
mamimum_range = int(input("Enter a number for maximum range: "))

# function to generate random numbers
def ran_num(num_range, minimum_range, mamimum_range):
    for _ in range(num_range):
        my_num = random.randint(minimum_range, mamimum_range)
        print("Random numbers are: ", my_num)
        
ran_num(num_range, minimum_range, mamimum_range)
