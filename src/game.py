import random
import words as w
import logic as l

def main_game_loop():
    playing = "yes"
    slices = 10
    print("Welcome to the Save the Watermelon! In this game, you will try to guess the hidden word \n"
          f"without losing all your watermelon slices. You will have {slices} slices to begin with. Each \n"
          "incorrect choice will destroy one slice, so be careful!")

    # this will loop through every word until user does not want to play anymore
    while playing == "yes":
        
        difficulty = l.choose_difficulty() # take input and validate
        incorrect = [] # list of user's incorrect guesses

        # takes a random word from the word list corresponding to the established difficulty
        secret = random.choice(w.word_list(difficulty)) 
        display_word = l.starting_display(secret) # starting display will have masked let      

        # this will loop through every user guess until user wins or slices = 0
        while slices > 0:
            
            if "_" not in display_word: # win condition
                print(f"\nCongratulations! You guessed the word: '{secret}'")
                break

            l.art(slices) # ASCII art of watermelon slices
            if len(incorrect) > 0: # will only display incorrect guesses if there is at least one
                print(f"Incorrect guesses: {", ".join(incorrect)}")

            # validates and converts user's guessed letter to lowercase
            guess = l.validate("letter",input(f"Hidden word: {display_word}. Guess a letter! : "))

            # if user's guess has been revealed, no change in score
            if guess in display_word: 
                print(f"'{guess}' has already been revealed.... Try again!")
            # if user already made that guess and it's incorrect, no change in score
            elif guess in incorrect:
                print(f"You already guessed '{guess}'. Try again!")
            # if guess was part of the secret word, the masked word updates to reveal it
            elif guess in secret:
                display_word = l.display_change(guess, secret, display_word)
                print("You guessed a correct letter!")
            # if guess doesn't qualify in all of the above, it's added to the incorrect list and score goes down
            else:
                incorrect.append(guess)
                print("Wrong. Try again!")
                slices -= 1

        # lose condition
        if slices == 0:
            print("You lost...")

        # validates and converts user's yes or no input to lowercase
        playing = l.validate("word", input("Would you like to play again? (yes/no): "))

    # exit message displays once exiting while loop for game
    print("Thank you for playing Save the Watermelon!")

if __name__ == "__main__":
    main_game_loop()
