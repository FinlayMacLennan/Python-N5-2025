currentmiles = int(input("Please enter you current miles"))
startmiles = int(input("Please enter you start miles"))
Kwrating = int(input("Please enter the kW rating for your current charing station"))


if Kwrating == 7:
    pricepermile = 0
elif Kwrating == 22:
    pricepermile = 0.005
else:
    pricepermile = 0.01

milestravelled = (currentmiles - startmiles)

startmiles = currentmiles

cost = (pricepermile*milestravelled)
print(cost)