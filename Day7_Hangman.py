
import random 
# Load word list with random words
word_list = ["aardvark", "baboon", "camel"]

# Select a random word from the word list
chosen_word = random.choice(word_list)
# Find the length of the chosen random  word
chosen_word_length = len(chosen_word)

 
print(f'Pssst, the solution is {chosen_word}.') 

# Create list and load it with blanks('_')
display = []

for testing in range(0,chosen_word_length):
    display.append('_')
    
# Tries equals the number of failed guesses the player is allowed
tries = 7   
 
# The main game loop and logic: 
while '_' in display and tries > 0:

    position = 0 
  
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        tries -= 1
        
    for letter in chosen_word:

        if letter == guess and display =='_':
            display[position] = guess
           # print(display)

        elif letter == guess:
            display[position] = guess
            
        # Used to cycle through each position in the display list    
        position +=1
        
        # For Debugging:
        print(display)
        print(tries)

        
# If player guesses all the correct laters while still having available tries, then the player Wins!   
# else the player loses
if '_' not in display and tries > 0:
    print('You Won!!!')
else:
    print('You Lose')    
             
