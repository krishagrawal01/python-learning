# try:
     # risky code

# except SomeError:
     # handle error

# else:
     # run if no error

# finally:
     # always run

# except ValueError:
# except ZeroDivisionError:
# except IndexError:
# except KeyError:
# except TypeError:
# except FileNotFoundError:

try: 
    num = int(input("Enter a number: "))

    print("Square of number is:", num * num)

except ValueError:
    print("Please enter a number.")

# except Exception as e:
#     print("Error:", e)

else:
    print("You entered:", num)

finally:
    print("Program finished")