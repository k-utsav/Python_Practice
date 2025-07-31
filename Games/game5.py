# Write a program that asks the user for a number and then calculates and prints the factorial of that number (e.g., for 5, output 5 × 4 × 3 × 2 × 1 = 120).

num = int(input("Enter a number: "))
# print(num)

factorial = 1
for i in range(1,num+1):
    # print (i)
    factorial *=i
    print(f"{num} x {i} = {factorial}")
    
print(f"The factorial of {num} is {factorial}")