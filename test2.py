def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    print("1:- Add")
    print("2:- Subtract")
    print("3:- Multiply")
    print("4:- Divide")

    choice = input("Choose an operation!")

    if choice == "1":
        print(add(num1 , num2))

    elif choice == "2":
        print(subtract(num1 , num2))

    elif choice == "3":
        print(multiply(num1 , num2))

    elif choice == "4":
        print(divide(num1 , num2))

    else:
        print("INVALID")

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("You cannot divide by zero!")
