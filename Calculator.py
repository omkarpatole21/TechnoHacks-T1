#Functions for addition,substraction ,multiplication,division
def add(x, y):
    return x + y


# It subtracts two numbers
def subtract(x, y):
    return x - y


# It multiplies two numbers
def multiply(x, y):
    return x * y


# It divides two numbers
def divide(x, y):
    return x / y


print("Select To calculate.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    ch = input("Enter the choice: ")

    # choose from the four options
    if ch in ('1', '2', '3', '4'):
        no1 = float(input("Enter Number1: "))
        no2 = float(input("Enter Number2: "))

        if ch == '1':
            print(no1, "+", no2, "=", add(no1, no2))

        elif ch == '2':
            print(no1, "-", no2, "=", subtract(no1, no2))

        elif ch == '3':
            print(no1, "*", no2, "=", multiply(no1, no2))

        elif ch == '4':
            print(no1, "/", no2, "=", divide(no1, no2))

        # check if user wants another calculation
        # break the while loop if answer is no
        calc= input("Continue Calculation?(yes/no): ")
        if calc== "no":
            break

    else:
        print("Invalid Input")