endings = ["ing","end","axe","gex","goh"]

StudentsNo = int(input("Please enter the number of stuents that you need usernames generated for"))

for i in range(StudentsNo):
    name = input("Please enter the first 3 letters of the students name")

    while len(name) != 3:
        print("Please enter 3 characters only")
        name = input("Please enter the first 3 letters of the students name")
    print("Thank you for entering the first 3 letters of the students name")

    username = (name, )