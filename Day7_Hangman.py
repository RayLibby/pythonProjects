#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random 

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ")


is_letter_in_word = ""
if guess in chosen_word:
 is_letter_in_word = "Yes"
else: 
 is_letter_in_word = "No"

print(f"You guessed: {guess}")
print(f"Is your letter in the word? {is_letter_in_word}")
print(f"The chosen word: {chosen_word}")
