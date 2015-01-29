#Goal: write a program that validates ISBN numbers

isbn_string = input("ISBN: ")

isbn_list = list(isbn_string)

length = 10

sum = 0

for x in range(0,length):
    current = int(isbn_list[x])
    sum += current * (length-x)

if sum%11 == 0:
    print("Valid ISBN code")
else:
    print("Invalid ISBN code")



