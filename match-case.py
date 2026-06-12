print("-----Calculator-----")

print("Choose the operation:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

choice = int(input("Enter your choice: "))

match choice: 
    case 1: 
        print("Addition is:", num1 + num2)
    case 2: 
        print("Subtraction is:", num1 - num2)
    case 3: 
        print("Multiplication is:", num1 * num2)
    case 4: 
        print("Division is:", num1 / num2)
    case _:
        print("Invalid Input")