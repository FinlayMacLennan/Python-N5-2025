#WireFrame 1

#Second Half Action
#==================

#Enter the home team half time score: _______
#Enter the away team half time score: _______

#Enter the home team full time score: _______
#Enter the away team full time score: _______


#The total number of goals scored after halftime is:
#<<toalscore>>

print("Second Half Action")
print("==================")

print("")

a = int(input("Enter the home team half time score: "))
b = int(input("Enter the away team half time score: "))

print("")

c = int(input("Enter the home team full time score: "))
d = int(input("Enter the away team full time score: "))

print("")

print("The total number of goals scored after halftime is:")

half = (a + b)
full = (c + d)

goal = (full - half)

print(goal)