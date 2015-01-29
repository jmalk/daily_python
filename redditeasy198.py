#Goal: two armies are shooting big words at each other across a valley. The
# words hit in the middle and all letters that don't cancel out with matching
#letters in the other word fall to the ground. Colliding 'hat' and 'cat' leaves
#you with 'c' and 'h'. Write a program that when given two words returns the
#leftover words

word1 = input("Word 1: ").lower()
word2 = input("Word 2: ").lower()

w1_letters = list(word1)
w2_letters = list(word2)

all_letters = list(word1+word2)
total_length = len(all_letters)

unique_letters = []

for x in range(0,total_length):
    
    letter = all_letters[x]

    n_left = w1_letters.count(letter)
    n_right = w2_letters.count(letter)

    if unique_letters.count(letter) == 0:
        if n_left != n_right:
            num_outstanding = abs(n_left-n_right)
            for y in range(0,num_outstanding):
                unique_letters.append(letter)

print(unique_letters)


    
