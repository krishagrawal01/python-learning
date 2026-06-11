fruit = "mango"

print(fruit)
print(fruit[4])
print(fruit[0:3])   #including 0 but not 3

len1 = len(fruit)
print(len1)

print(fruit[0:-3])              #both are same
print(fruit[0:len(fruit)-3])    #both are same

print(fruit[len(fruit)-3:len(fruit)-1])