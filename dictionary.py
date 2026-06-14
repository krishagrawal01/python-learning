student = {

    "name": "Krish",
    "age": 20,
    "branch": "CSE"
}

print(student["name"])    #gives error if key is not present
print(student.get("name"))    #doesn't gives error

student["sex"] = "male"     #we add more key value pair like this

print(student)

print(student.keys())
print(student.values())

info = {
    
    "name": "Krish",
    "age": 20,
    "branch": "CSE"
}

for key in info.keys():
    print(key)

for key in info:
    print(key)

for value in info.values():
    print(value)

for key in info.keys():    #prints value
    print(info[key])

for key, value in info.items():
    print(key, value)