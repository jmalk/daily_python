#Goal: accept a string of numbers and/or letters and say if it's a palindrome
# or not

test_string = input("Enter phrase: ")

test_list= list(test_string)

list_length = len(test_list)

if list_length%2 == 1:
    limit = int((list_length-1)/2)
else:
    limit = int(list_length/2)

palindromic = True

for y in range(0,limit):
    if test_list[y] == test_list[list_length-1-y]:
        pass
    else:
        palindromic = False
        break

if palindromic:
    print("Palindrome")
else:
    print("Not a palindrome")
