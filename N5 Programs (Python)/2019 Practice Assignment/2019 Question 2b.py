import random

final_usernames = []
endings = ["ing","end","axe","gex","goh"]

StudentsNo = int(input("Please enter the number of stuents that you need usernames generated for"))

for i in range(StudentsNo):
    name = input("Please enter the first 3 letters of the students name")

    while len(name) != 3:
        print("Error, Please enter 3 characters only")
        name = input("Please enter the first 3 letters of the students name")
    print("Thank you for entering the first 3 letters of the students name")

    end = random.choice(endings)
    final = name + end
    username = final

    final_usernames.append(username)

for i in range(StudentsNo):
    print(final_usernames[i])