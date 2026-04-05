# save-the-watermelon

Save the Watermelon is a game based off of the classic Hangman! This is a project for my Python class. 

## How to run
```
# Run
python -m src.game
# or
python src/game.py
```
## How to test
To test functions contained in the logic module, go into the test_logic module where 5 function tests are presented. Only the first function will take in a user input. The inputs for other functions will have to be manually changed in the code.

## Features & Rules
This game has 3 difficulties: easy, medium, and hard. Easy words are 3-5 letters long. Medium words are 6-7 letters long. Hard words are 8 or more letters long. Once you choose a difficulty, you will be presented with the masked version of a secret word from your difficulty. Medium and hard words will start with one letter already revealed. For instance, the word 'string' could be shown as \_\_\_i\_\_. You will start the game with 10 watermelon slices, which are your lives. As you guess letters in the secret word, you will lose a slice for every incorrect guess, or you will reveal a letter for every correct guess. Try to reveal the entire word before losing all your lives! Good luck!

## Limitations
The master list of words can be changed in the words.py file to include any additional words. The current master list only contains 91 words, with there being 43 in the easy list, 26 in medium, and 22 in hard. The user cannot choose the starting number of watermelon slices, but it can be changed in the game.py file, in the variable max_slices, which is automatically set to 10.
