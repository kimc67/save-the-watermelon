import logic as l

# will ask for user input
print(l.choose_difficulty())

# 1st paramter is the letter checked in the 2nd parameter, 3rd parameter is the starting display
print(l.display_change("a","applesauce","__________"))

# will convert every character of input into underscores
print(l.starting_display("applesauce"))

# will print any number of watermelon slices
l.art(30)

# 'word' in 1st parameter will validate 'yes' or 'no' in 2nd parameter
# 'letter' in 1st parameter will validate an alphabet character in 2nd parameter
print(l.validate("word","yes"))
