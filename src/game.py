import random
import words as w
import logic as l

def main_game_loop():
    playing = "yes"
    slices = 10
    print("Welcome to the Save the Watermelon! In this game, you will try to guess the hidden word \n"
          f"without losing all your watermelon slices. You will have {slices} slices to begin with. Each \n"
          "incorrect choice will destroy one slice, so be careful!")

    # this will loop through every game
    while playing == "yes":
        difficulty = l.choose_difficulty() # take input and validate
        incorrect = [] # list of user's incorrect guesses

        # takes a random word from the word list corresponding to the established difficulty
        secret = random.choice(w.word_list(difficulty)) 
        display_word = l.starting_display(secret) # starting display will have masked let      

        # this will loop through every user guess
        while slices > 0:
            if "_" not in display_word:
                print(f"\nCongratulations! You guessed the word: '{secret}'")
                break

            l.art(slices)
            if len(incorrect) > 0:
                print(f"Incorrect guesses: {", ".join(incorrect)}")

            guess = l.validate("letter",input(f"Hidden word: {display_word}. Guess a letter! : "))

            if guess in display_word:
                print(f"'{guess}' has already been revealed.... Try again!")
                continue
            elif guess in incorrect:
                print(f"You already guessed '{guess}'. Try again!")
            elif guess in secret:
                display_word = l.display_change(guess, secret, display_word)
                print("You guessed a correct letter!")
            else:
                incorrect.append(guess)
                print("Wrong. Try again!")
                slices -= 1

        if slices == 0:
            print("You lost...")

        playing = l.validate("word", input("Would you like to play again? (yes/no): "))

    print("Thank you for playing Save the Watermelon!")

if __name__ == "__main__":
    main_game_loop()
