# Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID
# and finger print

# Read the input from command line –Reference ID
i = input("Enter your password: ")

# Check for validity –it should be 12 digits and allows on number and alphabet

# Create your alpha bet and number lists
char_list = []
for k in range(65, 122):
    char_list.append(chr(k))

num_list = []
for l in range(0, 10):
    num_list.append(l)

spec_list = []
for m in range(35, 39):
    spec_list.append(chr(m))

# set up the loop to check the elements of your list align to alphabets and numbers and special characters.
list_i = list(i)
str_encrypt = []

if len(list_i) == 12:
    for j in range(len(list_i)):
        j_input = list_i[j]
        if j_input in char_list:
            pass
        elif j_input in str(num_list):
            pass
        elif j_input in spec_list:
            pass
        else:
            print("Incorrect Password Character entered")
        str_encrypt.append(j_input)

else:
    print("Password Character Count not equals to 12")
    str_encrypt.clear() # clear if conditions for password not met to ensure this list does not get into the next loop


str_encrypt2 = []
str_final = ''
if len(str_encrypt) != 0:
    i_2 = input("Do you want to see the encrypted version of your password: ")
    for n in range(len(str_encrypt)):
        if i_2 == 'Yes':
            i_encrypt = '@'
            str_final = str_final + i_encrypt

        else:
            i_encrypt = str_encrypt[n]
            str_final = str_final + i_encrypt
    print("Here is your password: " + str_final)
