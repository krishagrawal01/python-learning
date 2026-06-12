list = [1, 1, 2, 3, 5, 4, 8 ,7]

list.append(6)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
print(list.index(5))
print(list.count(1))
list.reverse()

list2 = list.copy()     #don't use list2 = list as it assign list2 to original list
                        #and does not create new list

list.insert(2, 55)
print(list)

fruit = ["Mango", "Banana", "Apple"]

newList = list + fruit

list.extend(fruit)
print(list)
