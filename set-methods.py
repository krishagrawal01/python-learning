s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)
print(s1.union(s2))    #here the original set is not changed
print(s1.update(s2))    #here the original set is updated

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1 & s2)
print(s1.intersection(s2))    
print(s1.intersection_update(s2))  

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1.symmetric_difference(s2))    
print(s1.symmetric_difference_update(s2))

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1 - s2)
print(s1.difference(s2))
print(s1.difference_update(s2))

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1.isdisjoint(s2))    #prints true is sets are disjoint

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

print(s1.issuperset(s2))    #prints true if s1 is superset 

#same for issubset

s1.add("Krish")

s1.update("For adding more than one item")

s1.remove("Krish")    #gives error when the item is not present
s1.discard("Krish")    #doesn't give error

print(s1.pop())    #pops random item from set

s1 = {1, 2, 3, 4,}
s2 = {3, 4, 5, 6, 7}

del s1    #deletes the set
s2.clear()    #empty the set


