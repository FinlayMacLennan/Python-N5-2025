# Task 1

# Create a program that contains an array of 7 daily temperatures (in celsius). 
# Traverse the 1D array to calculate and display the average temperature 
# (sum of 7 days/7).


tempretures = []

total = 0

for index in range(7): 
    tempretures.append(int(input("Enter todays tempreture")))
    total = (total+tempretures[index])

print(total/7)