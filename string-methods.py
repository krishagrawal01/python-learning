name = " Krish!!!"
fruit = "Mango,Apple,Banana"
car = "Mercedes BMW Volkswagon"

print(name)

print(name.upper())
print(name.lower())
print(name.strip()) 
print(name.rstrip("!"))

name.lstrip()   # remove from left
name.rstrip()   # remove from right
name.strip()    # remove from both sides

print(fruit.replace("M", "T"))
print(fruit.split(","))     #the character used to split gets removed
print(fruit.split("a"))

print(car.split())

print(car.capitalize())