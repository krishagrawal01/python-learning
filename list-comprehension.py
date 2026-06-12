evens = []

for i in range(1, 101):
    if i % 2 == 0:
        evens.append(i)

print(evens)

evens = [i for i in range(1, 101) if i % 2 == 0]    #list comprehension
print(evens)