''' Write a Python program that asks the user for a positive integer n. 
 Then, use a for loop to calculate and print the sum of all integers from 1 to n '''
 
total_sum = 0
num = int(input ("Enter a number: "))
print("The number entered is: ",num)

for i in range (1, num+1):
    total_sum = total_sum+i
    
print (f"the sum from 1 to {num}: ",total_sum)
    