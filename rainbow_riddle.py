# Create a list of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Ask the user to guess a color of the rainbow
guess = input("I am thinking of a color of the rainbow. Can you guess what it is? ")

# Check if the user's guess is correct
if guess.lower() == colors[3]:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, that is not the correct answer. The color I was thinking of was " + colors[3] + ".")
