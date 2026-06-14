words = ("cat", "bat", "mat")

l = list(words)     #we converted tuple to list to make changes in it

l.append("rat")
print(l.pop(2))     #removes element at given index and returns the removed element

words = tuple(l)

print(words)

morewords = ("map", "lap", "tap", "tap")

newtuple = words + morewords    #we can concatinate touple
print(newtuple)

print(newtuple.count("map"))
print(newtuple.index("tap"))