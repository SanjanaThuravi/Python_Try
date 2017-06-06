import random
import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

letter_input_1 = input("Enter which letter you want?v for vowel, c for consonants or l for any letter? \n")
letter_input_2 = input("Enter which letter you want?v for vowel, c for consonants or l for any letter? \n")
letter_input_3 = input("Enter which letter you want?v for vowel, c for consonants or l for any letter? \n")

def generator():
    if letter_input_1 == 'v':
        l1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        l1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        l1 = random.choice(letters)
    else:
        l1 = letter_input_1

    if letter_input_2 == 'v':
        l2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        l2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        l2 = random.choice(letters)
    else:
        l2 = letter_input_2

    if letter_input_3 == 'v':
        l3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        l3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        l3 = random.choice(letters)
    else:
        l3 = letter_input_3

    name = l1 + l2 + l3
    return name

for i in range(30):
    print(generator())