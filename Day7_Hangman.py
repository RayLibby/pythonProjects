#Step 1 
import random 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()
tries = chosen_word_length
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

''' 
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    
'''
 
print(f'Pssst, the solution is {chosen_word}.') 


display = []

for testing in range(0,chosen_word_length):
    display.append('_')


while '_' in display:

    position = 0     
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:

        if letter == guess and display =='_':
            display[position] = guess
           # print(display)

        elif letter == guess:
            display[position] = guess
           # print(display)
        #else:
            #print(display)
        print(display)
        position +=1
        #tries -= 1
              
#Testing code

'''
# print(display)       



  for letter in chosen_word:
        if letter == guess:
            display.append(guess)
        else:
            display.append('_')
'''


'''

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
guess = input("Guess a letter: ").lower()

# Split letter in chosen word
letters_to_list = []
for letter in chosen_word:
    letters_to_list.append(letter)




position=0
is_letter_in_word = []

for letters in letters_to_list:
    if guess in letters_to_list[position]:
        print("RIGHT")
    else:
        print("WRONG")

    position +=1

    
print(f"You guessed: {guess}")
print(f"The chosen word: {chosen_word}")
print(f"Length of word: {chosen_word_length}")
print(f"Is your letter in the word? {letters_to_list}")
'''