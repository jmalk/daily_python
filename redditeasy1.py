#Goal: take name, age and username as input, write them to a file, and output
# as part of a sentence

name = input("What is your name? ")
age = input("How old are you? ")
username = input("What is your reddit username? ")

fo = open("redditeasy1_datafile.txt","a+")
fo.write(name + "\t" + age + "\t" + username + "\n");
fo.close()

print("Your name is %s, you are %s years old, and your reddit username is %s" % (name,age,username))
