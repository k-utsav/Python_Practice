# WAP to find if the given num is prime or not

import math

first = int(input("Enter first num: "))
last = int(input("Enter last number: "))

def isPrime(num):
    isPrimeNum = True
    if num > 1:
        for i in range (2,int(math.sqrt(num))+1):
            if num%i == 0:
                isPrimeNum = False
                break
        if isPrimeNum:
            print (num, "is prime number.")
        else:
            print (num, "is not prime.")
    else:
        print("The number entered is less than 1 which is not a prime number")

# print ("The number is: ", (isPrime(num)))
for j in range (first, last):
    isPrime(j)
        

