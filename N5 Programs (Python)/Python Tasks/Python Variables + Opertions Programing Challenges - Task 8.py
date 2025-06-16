#Task 8: Sports Statistics
#Create a program for a football team that:

#Stores overall goals scored, overall goals conceded and number of games played
#Calculates goal difference
#If they played 10 games, calculate the average goals per game
#Display all relevant statistics

goalsscored = int(input("Enter goals scored"))
goalsconceded = int(input("Enter goals conceded"))
gamesplayed = int(input("Enter games played"))

goaldiffrence = (goalsscored-goalsconceded)

avarage = (goalsscored/10)

print("You scored", goalsscored)
print("You conceded", goalsconceded)
print("You Played", gamesplayed)
print("Your avarage goals scored over 10 games was", avarage)