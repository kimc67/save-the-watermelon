# Pseudocode

```
def main_game_loop:

  playing = yes
  display "welcome"

  while playing = yes:
    difficulty = input("choose difficulty")
    while difficulty is not easy, medium, or hard:
      input("invalid input, please choose easy, medium, or hard")
    if difficulty = easy:
      words = easy word list
    elif difficulty = medium:
      words = medium word list
    else:
      words = hard word list

    slices = 10
    incorrect = []

    secret = random choice from words
    display_word = "_" * length of secret
    if length of secret > 5:
      random_character = random choice from secret
      reveal_positions = [iterate secret with index i, if character is random_character]
      for i in range length of reveal_positions:
        display_word[reveal_positions[i]] = random_character

    while slices > 0:

      if "_" is not in the display_word:
        display "you won"
        break

      art_slices(slices)
      if length of incorrect > 0:
        display f"these are your incorrect guesses: {incorrect}"
      guess = input(f"{display_word}, make a guess")

      while guess is not one letter:
        guess = input("invalid input, please choose a letter")
      if guess is in display_word:
        display f"{guess} has already been revealed"
        continue
      elif guess is in secret:
        positions = [iterate secret with index i, if character is guess]
        for i in range length of positions:
          display_word[reveal_positions[i]] = guess
        display "correct", display_word
      else:
        append guess to incorrect
        display "incorrect"
        slices -= 1

    if slices = 0:
      display "you lost"

    playing = input("would you like to play again?")
    while playing is not yes or no:
      playing = input("invalid input, enter yes or no")

  display "thank you for playing the game"
```
