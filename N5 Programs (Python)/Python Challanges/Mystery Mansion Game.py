# N5 Python Programming Challenge - Mystery Mansion

# Create a simple text-based adventure game called "The Mystery Mansion" where players can explore four different locations.

# Your program must demonstrate understanding of 1D arrays, input validation, and string concatenation

# Your adventure takes place in a mysterious mansion with these four rooms:

# Entrance Hall - "A grand foyer with a crystal chandelier"
# Library - "Dusty bookshelves stretch from floor to ceiling"
# Kitchen - "Copper pots hang above an old stone hearth"
# Garden - "Overgrown vines twist around marble statues"

# Technical Requirements
# 1. 1D Arrays

# Location Names Array: Store the four location names
# Location Descriptions Array: Store detailed descriptions for each location
# Available Commands Array: Store valid player commands (N, S, E, W, quit, help)

# 2. Input Validation

# The valid directions are north (N), south (S), east (E) and west (W).
# If the user enters anything that isn’t a valid command or direction, display a helpful error message.

# 3. String concatenation

# You should combine the location name and description when displaying this to the player.
# You should create a personalised welcome message using the player’s name

rooms = ["Enterence Hall", "Libary", "Kitchen", "Garden"]
descriptions = ["A grand foyer with a crystal chandelier", "Dusty bookshelves stretch from floor to ceiling",
                 "Copper pots hang above an old stone hearth", "Overgrown vines twist around marble statues"]
commands = ["N", "S", "E", "W", "Quit", "Help"]
help = ("Please enter either 1 (North), 2 (South), 3 (East), 4 (West) to move through the masion. Only type the letters not the names.")

name = input("Please Enter you Player Name")

print("Welcome", name, "To the Mystery Mansion")
print("To exploar the mysterious mansion Please enter either N (North), S (South), E (East), W (West) to move through the masion.")
print("If you want to quit the game enter  Quit and if you need the commends enter help")
print("Please now enter the commands to move throught the manison")


while True:
    move = input("Please enter where you would like to move to")
    if move == commands(0):
            print("Welcome to the",rooms(0) + descriptions(0))
    elif move == commands(1):
            print("Welcome to the",rooms(1) + descriptions(1))
    elif move == commands(2):
            print("Welcome to the",rooms(2) + descriptions(2))
    elif move == commands(3):
            print("Welcome to the",rooms(3) + descriptions(3))
    elif move == commands(4):
            quit()
    elif move == commands(5):
            print(help)
    else:   
            print("Not a valid move please try again, enter Help for the commands to the game") 