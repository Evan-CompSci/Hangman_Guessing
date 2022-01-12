import random

words_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(words_list)

hyphens = len(chosen_word)

if hyphens == 6:
    guess = "------"
elif hyphens == 4:
    guess = "----"
elif hyphens == 10:
    guess = "----------"

print('H A N G M A N')
print()
lives = 0



while lives < 8:
    print(guess)
    print('Input a letter:')
    letter = input()
    if letter in chosen_word:
        position = chosen_word.find(letter)
        guess = guess[:position] + letter + guess[position + 1:]
        if letter in guess:
            lives = lives + 1
    else:
        print("That letter doesn't appear in the word")
        print()
        lives = lives + 1

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
#print(chosen_word)
#print(hyphens)
