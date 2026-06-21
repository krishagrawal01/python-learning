class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age:"))

    if(age < 0):
        raise InvalidAgeError("Age cannot be negative")

except InvalidAgeError:
    print("Please enter a valid age")

except ValueError:
    print("Please enter a number")