# Program 2 - Investigate and Modify

#How can we change the program so that it asks for and stores 3 full names in the name array?

name = []

for index in range(1,4):
    firstname = input("Enter your first name:")
    surname = input("Enter your surname:")
    fullname = firstname + " " + surname
    name.append(fullname)

print(name)