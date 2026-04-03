# Pseudocode

```
def main_game_loop:

  display "welcome":

    while playing = yes:
      display "choose difficulty"
        if difficulty = easy:
          words = easy word list
        elif difficulty = medium:
          words = medium word list
        elif difficulty = hard:
          words = hard word list
        else:
          display "invalid input"
          continue
      secret = random choice from words
      slices = 10

      while slices < 10:
        display_word = "_" * length of secret
        random_character = random choice from secret
        reveal_positions = [iterate secret with index i, if character is random_character]
        for i in range length of reveal_positions:
          display_word[reveal_positions[i]] = random_character

```
