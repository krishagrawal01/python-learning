student = {

    "name": "Krish",
    "age": 20,
    "branch": "CSE"
}

student.update({"age": 21})
student.update({"gender": "male"})

# student.clear()

student.pop("name")
student.popitem()    #removes last key value pair

del student["name"]    #if key is not provided it deletes the entire dict


