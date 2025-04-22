import re
import utils

# initialize all variables

lives = 6
secretWord = []

# Choose a word bewtween 2 - 8 letters long.

uncutWord = utils.getWordFromAPI()

# Convert the word in the variable word to a list named actualWord

actualWord = (uncutWord.strip(r'.'))

#Hi

# create a list that is the same length as the word but filled with underscores. Name this list secretWord

secretWord = utils.convertWordToSecret(actualWord)

# The user puts it there first guess. Check the length of the users guess to ensure that it is 1 letter

print (f'Welcome to Hangman you have a {len(secretWord)} letter long word\n{secretWord}')
userGuess = str(input("Enter You Guess(pls)"))
if len(userGuess) > 1:
    print ("No")
    exit()

# Make a for loop to compare the letter that the user guessed to each letter in the list
## Within the for loop, do the following:
## Run the for loop for the length of the list
## Compare the character that the user guessed to each items in the list actualWord. 
## Cycle through the actualWord list using the iteration variable in the for loop
## if the character that the user typed is the same as the character in the actualWord at that location, If the userInput == actualWord[i], Then secretWord[i] = userInput
## Compare secretWord to actualWord
## When they are the same Break from the for loop  
## Break when the user runs out of guesses (i.e. when Lives = 0)
## If user is incorrect Lives -= 1
## Print secretWord again and lives left


#If the user fails to guess the word, computerPermissionToBullyUser = True


#
       
