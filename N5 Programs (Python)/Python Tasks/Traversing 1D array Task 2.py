# Task 2

# Create a program that contains an array of 5 dog food weights 
# (in grams) between 0 and 300g. Traverse the 
# 1D array to calculate and display the total amount
# of food given to the dog over 5 days.

food = []

total = 0

for index in range(5):
    food.append(int(input("Enter the dog food weight (between 0g and 300g)")))
        if food[index] > 0:
            print("Must be between 0g and 300g")
        elif food[index] < 300:
            print("Must be between 0g and 300g")
    total = (total+food[index])

print(total)