# This calculator was coded by Sami Elsayed

# Code all the operations/functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponent(x, y):
    if input == "yes":
        return x ** y
    else:
        return x ** 2


def floor(x, y):
    return x // y


def absolute(x):
    return abs(x)


# This prints the operations
print("Select an operation: \n")
print("Addition \n")
print("Subtraction \n")
print("Multiplication \n")
print("Division \n")
print("Exponent \n")
print("Absolute Value")

while True:
    choice = input("Enter choice: ")
    if choice in ('Addition', 'Multiplication', 'Subtraction', 'Division', 'Absolute Value', 'Exponent'):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))

        if choice == 'Addition' or 'addition' or 'add' or 'Add':
            print(number_one, " + ", number_two, " = ", add(number_one, number_two))

        elif choice == 'Subtraction' or 'subtraction' or 'subtract' or 'Subtract':
            print(number_one, " - ", number_two, " = ", subtract(number_one, number_two))

        elif choice == 'Multiplication' or 'multiplication' or 'multiply' or 'Multiply':
            print(number_one, " * ", number_two, " = ", multiply(number_one, number_two))

        elif choice == 'Division' or 'division' or 'divide' or 'Divide':
            print(number_one, " / ", number_two, " = ", divide(number_one, number_two))

        elif choice == 'Exponent' or 'exponent':
            print(number_one, "", number_two, " = ". exponent(number_one, number_two))

        elif choice == 'Absolute Value' or 'absolute value' or 'abs' or 'Absolute value':
            print("|" + number_one + "|" + " = ")

        # If the user wants another calculation
        next_calculation = input("Another calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
