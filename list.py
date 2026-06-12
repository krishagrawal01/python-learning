fruits = ["Apple", "Mango", "Banana", "Lichi", "Papaya", "Berries"]

print(fruits[0])

fruits[0] = "Guava"

print(fruits[0])

fruits.append("Grapes")
fruits.append("Strawberry")

if "Mango" in fruits:
    print("Yes")
else:
    print("No")

if "M" in "Mango":
    print("Yes")
else:
    print("No")

print(fruits[0:len(fruits):2])
