
import random 
from Day7_Hangman_Art import stages
from Day7_Hangman_Art  import logo 
from Day7_Hangman_Words import word_list
import os                     


print(logo)

# Load word list with random words


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
lives = 6   
 
# The main game loop and logic: 
while '_' in display and lives > 0:
    # Used to cycle through each position in the display list    
    position = 0 
    # Player's input
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    
    # If player guesses wrong they lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that is not in the word. You lose a life.')
    
    # If a player guesses the same correct letter twice, no points deducted    
    if guess in display:
        print(f"You've already guess {guess} ")    
        
    for letter in chosen_word:

        if letter == guess and display =='_':
            display[position] = guess
           # print(display)

        elif letter == guess:
            display[position] = guess
            
        # Used to cycle through each position in the display list    
        position +=1
        
        # For Debugging: indent these parameters so that they are inside the main for loop
    print(f'Number of Lives Left: {lives}')
    print(display)  
    print(stages[lives])
        
# If player guesses all the correct laters while still having available tries, then the player Wins!   
# else the player loses
if '_' not in display and lives > 0:
    print('You Won!!!')
else:
    print('You Lose!!!')    
             
