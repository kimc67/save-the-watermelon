# Test Plan

## Test matrix
| Input | Choosing difficulty | Make a guess | Play again? |
| -------- | -------- | -------- | -------- |
| easy/medium/hard | valid | invalid | invalid |
| yes | invalid | invalid | "Choose a difficulty" |
| no | invalid | invalid | "Thank you for playing" |
| other words | invalid | invalid | invalid |
| alphabet character | invalid | valid | invalid |
| any other character | invalid | invalid | invalid |
| no input | invalid | invalid | invalid |
| correct guess | N/A | "You guessed a correct letter" | N/A |
| incorrect guess | N/A | "Wrong" | N/A |
| repeated guess | N/A | "Already guessed" | N/A |

## Manual test transcript
```
# Choosing difficulty: yes/no, then other words, then alphabet character, then other character, then no input
Choose a difficulty level (easy / medium / hard): yes
Enter easy, medium, or hard: word
Enter easy, medium, or hard: c
Enter easy, medium, or hard: 3
That is a number. Enter easy, medium, or hard: 
Enter easy, medium, or hard: 
Enter easy, medium, or hard: 

# Choosing difficulty: easy/medium/hard
Choose a difficulty level (easy / medium / hard): easy

You have 10 slices left.

# Make a guess: easy/medium/hard, then yes/no, then other words, then other characters, then no input
Hidden word: _____. Guess a letter! : easy
Enter only one letter: yes
Enter only one letter: word
Enter only one letter: 3
That is a number. Enter a letter (a-z or A-Z): 
Enter a letter (a-z or A-Z): 
Enter a letter (a-z or A-Z): 

# Make a guess: alphabet character (correct)
Hidden word: _____e. Guess a letter! : l
You guessed a correct letter!

# Make a guess: alphabet character (incorrect)
Hidden word: _____e. Guess a letter! : r
Wrong. Try again!

# Make a guess: alphabet character (correct repeated guess)
Hidden word: _____e. Guess a letter! : e
'e' has already been revealed and it is correct.... Try again!

# Make a guess: alphabet character (incorrect repeated guess)
Incorrect guesses: r
Hidden word: _____e. Guess a letter! : r
You already guessed 'r' and it is wrong. Try again!

# Play again? : easy/medium/hard
Would you like to play again? (yes/no): easy
Enter yes or no: word
Enter yes or no: c
Enter yes or no: 3
That is a number. Enter yes or no: 
Enter yes or no: 
Enter yes or no:

# Play again? : yes
Enter yes or no: yes

Choose a difficulty level (easy / medium / hard):

# Play again? no
Would you like to play again? (yes/no): no
Thank you for playing Save the Watermelon!
```
