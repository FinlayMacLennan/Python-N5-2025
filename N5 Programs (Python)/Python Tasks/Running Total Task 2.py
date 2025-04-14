#Task 2

#Create a program that asks the user to input 5 test scores and calculates the running total after each input.

total = 0

for index in range(5):

    score = int(input("Please enter the test score:"))

    total = total + score

    print(total)

print("Your total test scores is:",total)