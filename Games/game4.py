# Create a program that prompts the user to enter a number. The program should then print the multiplication table for that number, from 1 up to 10.

num = int(input("Enter a number: "))
print("Below is the multiplication of the number: ",num)

for i in range(1,11):
    result = num*i
    # print(result)
    print(f"{num} x {i} = {result}")
