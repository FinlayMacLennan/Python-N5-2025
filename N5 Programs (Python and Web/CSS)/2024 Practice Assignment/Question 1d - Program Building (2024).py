# Step 1 - Initialising Variables

import random
total = 0
song_length = []

# Step 2 - Input Validation of training session

training_session = int(input("Please enter the length of your training session: "))
while training_session < 10 or training_session > 30:
    print("Error. A training session must be between 10 and 30")
    training_session = int(input("Please enter the length of your training session: "))

# Step 3 - Minutes to seconds

training_session = training_session * 60

# Step 4 - Total length of songs

song_counter = 0

while total < training_session:
    duration_of_next_song = int(input("Please enter the duration of your next song in seconds: "))
    total = total + duration_of_next_song
    song_length.append(duration_of_next_song)
    song_counter = song_counter + 1

    if total >= training_session:
        print("You have entered enough songs")

# Step 5 - Training session summary

counter = 1
foam_machine = random.randint(1, song_counter)

print("The number of songs you have played is", song_counter)

for i in range(len(song_length)):
    print(counter, ":", song_length[i])

    if foam_machine == counter:
        print("Start Foam Machine")

    counter = counter + 1                     

print("Your total is", total)