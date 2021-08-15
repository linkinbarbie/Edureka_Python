# 1.What is the Output of following code:
# Answer: 4. Set only takes unique elements and even though
# nums is in a list it is embedded in a set

# 2. What will be the output
# Answer: john
#  peter

# 3. Write a program to test the validity of a password given by a user

# 1. Input your password:
test = input("Enter your password: ")
list1 = list(test)  # convert to list to make iterable

# 2.  create the lists you want to use for comparison:
# 2a. alphabet using ASCII codes
upper_alphabet = []
for i in range(65, 91):
    upper_alphabet.append(chr(i))

# create alphabet list using ASCII
lower_alphabet = []
for i in range(97, 122):
    lower_alphabet.append(chr(i))

# 2c. list for numbers range
numbers = []
for i in range(0, 10):
    numbers.append(int(i))
numbers1 = str(numbers)
print(type(numbers1))

# 2d. list of special characters
spec_char = []
for i in range(35, 65):
    spec_char.append(chr(i))

lower_list = []
upper_list = []
num_list = []
sp_list = []
tup_final = ()
if 6 <= len(list1) <= 12:  # check the count of the elements in the password list
    for i in range(len(list1)):
        lst = list1[i]  # get each element in the password list
        if lst in lower_alphabet:
            lower_list.append(lst)
        elif lst in upper_alphabet:
            upper_list.append(lst)
        elif lst in numbers1:
            num_list.append(lst)
        elif lst in spec_char:
            sp_list.append(lst)
        else:
            empty = []
    tup_final = (lower_list, upper_list, num_list, sp_list)
    if [] in tup_final:
        print("Password is wrong")
    else:
        print("Password is correct")


else:
    print("Count of Password Characters is incorrect")


# 4. Write a for loop that prints all elements of a list and their position in the list
a = [4, 7, 3, 2, 5, 9]
for i in range(len(a)):
    lst = a[i]
    print(i)
    print(lst)
