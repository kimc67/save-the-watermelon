import random

def choose_difficulty():
    difficulty = input("\nChoose a difficulty level (easy / medium / hard):")
    while difficulty not in ["easy", "medium", "hard", "Easy", "Medium", "Hard"]:
        difficulty = input("Enter easy, medium, or hard: ")
    if difficulty == "easy" or difficulty == "Easy":
        return "easy"
    elif difficulty == "medium" or difficulty == "Medium":
        return "medium"
    else:
        return "hard"

def display_change(letter, word, display):
    display_list = list(display)
    positions = [i for i, char in enumerate(word) if char == letter]
    for i in range(len(positions)):
        display_list[positions[i]] = letter
    display = "".join(display_list)
    return display

def starting_display(word):
    display = "_" * len(word)
    if len(word) > 5:
        display_change(random.choice(word), word, display)
    return display

def art(slices):
    print(f"\nYou have {slices} slices left.\n", r"  /\  " * slices, "\n", r" /,'\ " * slices, "\n", "(____)" * slices)

def validate(letter_or_word,entry):
    if letter_or_word == "letter":
        while not entry.isalpha():
            entry = input("Enter a letter:")
        while len(entry) != 1:
            entry = input("Enter only one letter:")
    if letter_or_word == "word":
        while entry.lower() != "no" and entry.lower() != "yes":
            entry = input("Enter yes or no: ")
        while not entry.isalpha():
            entry = input("Enter a yes or no:")
    return entry.lower()
