#1. Arbitrary argument
# def sumOf(*numbers):
#     print("sum is:", sum(numbers))

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))

# sumOf(a, b, c)

#2. Keyword arbitrary argument
def student(**details):
    print(details)

student(name = "Krish", age = 20)