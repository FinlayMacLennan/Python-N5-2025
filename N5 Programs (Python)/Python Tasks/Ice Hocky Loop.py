#This program is a simulation of an ice hockey scoreboard.

home = 0
away = 0
period = 1

while period <= 3:
    print("---------------")
    print("Home -",home,"-",away,"- Away")
    print("Period",period)
    print("---------------")
    print()
    option = input("Enter (h)ome, (a)way or (x) to end period")
    while option != "h" and option != "a" and option != "x":
        print("Incorrect option, Try again.")
        option = input("Enter (h)ome, (a)way or (x) to end period:")
    if option == "x":
        period = period + 1
    elif option == "h":
        home = home + 1
    elif option == "a":
        away = away + 1
    elif period == 4:
        print("The Game has finished")