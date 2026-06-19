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
def squareNum(num):
     try:
          return int(num) * int(num)

     except ValueError:
          return "Please enter a number."

     # except Exception as e:
     #     print("Error:", e)

     # else:
     #      print("You entered:", num)    #runs only if error happens

     finally:
          print("Runs even after function returns a value")

num = input("Enter a number: ")

print(squareNum(num))