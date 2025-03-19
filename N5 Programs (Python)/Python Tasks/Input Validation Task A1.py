list = []

while True:

    percentage = int(input("Enter Percentage"))

    while percentage < 0 or percentage > 100:
        print("Error, % must be between 0 and 100")
        percentage = int(input("Enter Percentage"))

    list.append(percentage)
    print("Your input % is",list)