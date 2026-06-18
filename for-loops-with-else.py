numbers = (10, 20, 30, 40 ,50)

num = int(input("Enter a number: "))

for number in numbers:
    if num == number:
        print("Found")
        break
else:
    print("Not found")    #executes only after loop is completed