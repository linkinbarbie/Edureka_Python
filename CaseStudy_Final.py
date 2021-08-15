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
        print("Password is wrong. Insert the correct format.")
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

# 5 Please write a program which accepts a string from console and print the characters that have
# even indexes


i = input("Enter the text: ")  # input the text
list_input = list(i)  # make the test iterable
# print(list_input)

list_output = []  # create the list to capture the values of the even indexes
for index in range(0, len(list_input)):  # check each index
    if index % 2 == 0:  # check if the index is even
        lst_op = list_input[index]  # output the value and use it to create a new list
        list_output.append(lst_op)
# print(list_output)

print("Here is the output of even only indices: " + ''.join(list_output))  # using the join keyword concatenate the
# list values and remove ',' to make a string

# 6 Please write a program which accepts a string from console and print it in reverse order

inputText = input("Enter the text for reversal: ")
print("The reverse is " + inputText[::-1])

# 7 Please write a program which count and print the numbers of each character in a string input by console.
i = input("Enter the text you want to count: ")
i_list = list(i)
i_set = sorted(set(i))
print(sorted(i_set))

for index in range(len(i_set)):
    i_output = i_set[index]
    print(i_output + "," + str(i_list.count(i_output)))

# 8 With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
# write   a program to make a list whose elements are
# intersection of the above given lists

list_1 = [1, 3, 6, 78, 35, 55]
list_2 = [12, 24, 35, 24, 88, 120, 155]

set_l1 = set(list_1)  # convert list to set to use intersect
set_l2 = set(list_2)
set_l3 = set_l1 & set_l2
print(list(set_l3))  # print output in list format

# 9 With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all
# duplicate values with original order reserved

list_3 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
set_l4 = set(list_3)
list_l1 = list(set_l4)
print(list_l1[::-1])

# 10.By using list comprehension,
# please write a program to print the list after
# removing the value 24 in [12,24,35,24,88,120,155].

list_5 = [12, 24, 35, 24, 88, 120, 155]

list_7 = []
for index in range(len(list_5)):
    list_6 = list_5[index]
    if list_6 == 24:
        pass
    elif list_6 != 24:
        list_7.append(list_6)

print(list_7)

# 11.By using list comprehension, please
# write a program to print the list after removing the 0th,
# 4th,5th numbers in [12,24,35,70,88,120,155]

list_5 = [12, 24, 35, 24, 88, 120, 155]

list_8 = []
for index in range(len(list_5)):
    if index == 0:
        pass
    elif index == 4:
        pass
    elif index == 5:
        pass
    else:
        list_9 = list_5[index]
        list_8.append(list_9)
print(list_8)

# 12.By using list comprehension, please write a program to print the list after removing
# delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
list_5 = [12, 24, 35, 70, 88, 120, 155]

list_8 = []
for index in range(len(list_5)):
    list_10 = list_5[index]
    if list_10 % 5 == 0 and list_10 % 7 == 0:
        pass
    else:
        list_9 = list_5[index]
        list_8.append(list_9)
print(list_8)

# 13. Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,
# which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
list_counter = []
list_final = []
for index in range(1, 1000):
    if index % 5 == 0 and index % 7 == 0:
        list_counter.append(index)

for index in range(len(list_counter)):
    if index <= 5:
        ll = list_counter[index]
        list_final.append(ll)
    else:
        pass

print(list_final)

# 14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1
# with  a  given  n  input  by console (n>0).


