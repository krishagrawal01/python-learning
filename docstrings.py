def add(num1, num2):

    '''
    This is a 
    docstring
    '''
    return num1 + num2

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("Sum is:", add(num1, num2))

print(add.__doc__)    #is used to access docstring

#pep8 stands for python enhancement proposal

#the zen of python using import this