num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))


def addition():
    add = num1 + num2
    print(add)
    return add 
    
def mul():
    m = num1 * num2
    print(m)
    return m

def sub():
    s = num1 - num2
    print("The substraction of num1 & num2 is: ", s)
    return s    

addition()
sub()
mul()