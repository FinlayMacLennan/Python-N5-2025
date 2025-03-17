# Program 3 - Investigate and modify

password = input("Please enter your password: ")
while len(password) < 8:
    print("Error! Please enter a password longer then 8 characters, Thank you.")
    password = input("Please enter your password: ")
print("Password accepted.")