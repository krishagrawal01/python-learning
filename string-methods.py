name = " Krish!!!"
fruit = "Mango,Apple,Banana"
car = "Mercedes BMW Volkswagon"
s = "welcometomyworld"

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
print(car.center(50))
print(fruit.count("an"))
print(fruit.endswith("ana"))
print(fruit.endswith("go", 3, 5))
print(fruit.find("go"))     #gives -1 when given string is not found
print(fruit.index("go"))    #gives error
print(s.isalnum())      #checks if string is alphanumeric or not
print(s.isalpha())
print(s.islower())
print(name.isprintable())   #gives false if string contain non-printable ch like \n
print(name.isspace())   #gives true is string only contain white spaces
print(car.istitle())    #gives true if all the words only starts with capital
print(fruit.startswith("Ma"))
print(s.upper())
print(fruit.swapcase())
print(car.title())
