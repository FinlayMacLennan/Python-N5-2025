import random

counter = 0
mystory_fruits = ["apple","bananna","blueberry","kiwi","mango","orange","peach","pineapple","raspberry","strawberry"]
user_fruits = []
decision = "Y"

while decision == "Y" and counter < 6:
    fruits = str(input("Please enter your choice of fruit"))
    while len(fruits) <= 4:
        print("invalid fruit, please enter a fruit with more then 4 characters")
        fruits = str(input("Please enter your choice of fruit"))
    counter = counter + 1
    user_fruits.append(fruits)
    decision = str(input("Do you want to enter another fruit? - Please enter Y/N"))

number =  random.randint(0,9)
print("The fruits you entered were")
print(user_fruits)
print("The mystery fruit was")
print(mystory_fruits[number])

counter = counter + 1

if counter < 3:
    print("You have a milkshake")
elif counter == 3 or counter == 4:
    print("you have a smoothie")
else:
    print("You have a fruit juice")