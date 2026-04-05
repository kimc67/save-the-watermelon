# Design

## Problem Statement
I need to program a game called "save the watermelon" which is a word-guessing game that displays watermelon slices as lives. The target audience is anyone who can spell common words.

------------------------------------------------------------------------

## Rules
The player is presented with a masked version of a randomly picked word and a set amount of watermelon slices. Then they guess a letter for every round. If they choose a letter that is part of the word, that letter is revealed. Otherwise, if they choose an incorrect letter, the watermelon slice counter decreases by one. 

**How to win:** The player wins if they reveal the entire word before the slice counter goes to zero.
The player loses if the slices reach zero.

------------------------------------------------------------------------

## Core features
I must include a set of all possible words that could be picked for each game. There should be a sufficient amount of words so that words don't repeat often between games. I must also create a watermelon slice counter with a set amount of slices for each game. I must show the player their previous incorrect guessed letters. After each game, I must display a menu for the player to choose between exiting or replaying the game.

### Stretch goals
It would be nice to have an aesthetically pleasing design for the watermelon slices, perhaps by converting watermelon art into ASCII characters. It would also be more fun to include different levels of difficulty. I could implement this by separating my word list into short, medium, and long words.

------------------------------------------------------------------------

## Flow 
1. Welcome message
2. Prompt user to choose difficulty
3. Display starting masked word
4. Prompt user for guess
5. Masked word or slice counter updates
6. Steps 4-5 repeat until player guesses all letters or loses all slices
7. Display win/loss message
8. Prompt user to exit or restart
9. If restart, steps 2-8 repeat

## Data design
Depending on the number of difficulty levels I implement, words will be stored in the same amount of word lists as difficulty levels. These will be lists of strings. If I only do one difficulty, there will only be one word list. 

The random module will be used for the next steps. At the start of every game, a string is selected at random from a word list. This string will be displayed to the user as a string of underscores that represent each letter. Any string longer than five characters will have at least one letter revealed at random. To do this, a random character will be chosen from the word and then revealed in the masked word.

If the player guesses a correct letter, the underscores that represented that letter will be replaced by the correct letter. If they guess a wrong letter, their slice counter, will decrease by one. Since it is ASCII art, the string corresponding to the slice count will be updated to match the current slice count. 

## Module/function responsibility
The logic module will contain all the functions I described above. The words module will include the word list(s) that I will implement in the game. These modules will be imported into the game module, which will have the menu loop, gameplay loop, and takes in inputs. They will be stored in the src package. The only other module used will be the random module. 
