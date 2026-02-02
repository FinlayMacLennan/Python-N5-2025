fruits = ["apple","bananna","blueberry","kiwi","mango","orange","peach","pineapple","raspberry","strawberry"]
user_fruits = []

number_of_fruits = int(input("Please enter the number of fruits you want"))

for index in range(number_of_fruits):
    choice = str(input("Please enter each fruit"))
    while len(choice) < 4:
        print("Invaild choice, fruits must be equal to or more then 4")
        choice = str(input("Please enter each fruit"))
user_fruits.append(choice)