from pyparsing import nums


def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def avg(num1,num2):
    return (num1+num2)/2

print("\nPlease select a operation: ")
print("1. Addition ")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")

select = int(input("Enter a number = "))
number1 = int(input("Enter the first number = "))
number2 = int(input("Enter the second number = "))

if select == 1:
    print(number1, "+", number2, "=", add(number1,number2))

elif select == 2:
    print(number1, "-", number2, "=", sub(number1,number2))

elif select == 3:
    print(number1, "*", number2, "=", mul(number1,number2))

elif select == 4:
    print(number1, "/", number2, "=", div(number1,number2))

elif select == 5:
    print(number1, "+", number2, "/", "2", "=", avg(number1,number2))

else:
    print("Invalid ")