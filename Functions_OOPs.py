from functools import reduce


# Function Definition and Call
# Function Definition
def print_name(stg):
    print("Welcome to Python, ", stg)
    return ()


# Function call
stg = input("Enter your name: ")
print_name(stg)


# Return statement terminates the execution of a function and returns control to the calling function

def add(a, b):
    sums = a + b
    return sums


num1 = input("Enter first number")
num2 = input("Enter second number")
n1 = int(num1)
n2 = int(num2)
ans = add(n1, n2)
print("Addition of 2 numbers is:", ans)


# Concept of __name__ == "__main__"
def func():
    print("func() in one.py")


print("top-level in one.py")

if __name__ == "__main__":
    print("functions_oops.py is being run directly")
else:
    print("functions_oops.py is being imported into another module")

# Important Built In Function
# Enumerate returns a list of tuples. Tuples consists index values and items from the list

# onsists index values and items from the list
grocery = ["bread", "milk", "butter"]
enumerateGrocery = enumerate(grocery)

# Return an enumerate object. The iterable must be a sequence, an iterator,
# some other object that supports iteration

print(type(enumerateGrocery))
# class is enumerate

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# Lambda Function
# Lambda functions are called when we require a nameless function for a short time

ans = (lambda z: z * 4)
print(ans(7))

# map - applies a function to all items in an input list
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)

# filter - filter creates a list of elements for which a function returns true
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

first = 1
second = 3
ans = (lambda x, y: x * y)  # tip the variables are in scope so will not see the variables outside
print(ans(first, second))

# reduce  - useful function for performing some computation on a list and returning the result

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

# Scope of a variable

# Global Variable

a = 50  # global variable


def number():
    b = 30  # local variable because it is defined and only be called within the function
    print(b)


print(a)
number()


# Required Arguments

def print_names(st):
    print("Welcome to Python, ", st)
    return ()


print_names()  # in this case argument is omitted which will cause an error


# Keyword Arguments

def welcome(str):
    print("Welcome to Python, ", str)
    return ()


welcome(str="Annie")


# part 2:
def adding(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)
    sums = a + b + c + d
    return sums


ans = adding(a=10, b=12, c=14, d=16)  # Integer values are passed as arguments when the function is called
print("Sum is :", ans)


# Default Arguments
# A default argument assumes a default value if a value is not provided in a function call for that argument

def info(name, age=50):
    print("Name : ", name)
    print("Age :", age)
    return ()


info(age=24, name="Ngozi")
info(name="Roland")  # age is not passed when the function is called. The function takes default value of age


def employee(name, id, salary=10000):
    print("Name of employee: ", name)
    print("ID no of employee: ", id)
    print("Salary of employee: ", salary)


employee("Sara", 101, 20000)
employee("Alex", 98)


# Variable length arguments

def infos(user, *users):
    print("Users of Python: ")
    print(user)
    for var in users:
        print("Users of Python")
        print(var)
        return ()


infos("Annie")
infos("Annie", "Dave", "Roland")


def myFunction(arg1, arg2, arg3, *args, **kwargs):
    print("First Normal Argument :" + str(arg1))
    print("Second Normal Argument :" + str(arg2))
    print("Third Normal Argument :" + str(arg3))
    print("Non-keyword argument :" + str(args))
    print("Keyword Argument :" + str(kwargs))


myFunction(1, 2, 3, 4, 5, 6, 7, name="Mnadar", country='India', age=25)


# when you pass a dictionary it is collected in a function using **kwargs

# Class and Objects

# Class is a blueprint used to create objects having the same property or attribute as its class
# object is an instance of a class which contains variables and methods

class number():
    pass



x = number()
print(x)


# self points to the class. ob is the object of class.

class edureka():
    def hello(self):
        print("Happy Learning")


ob = edureka()
ob.hello()

# Scope of Variables in class
a = 30


class edureka():
    b = 90
    print(b)


ob = edureka()
1