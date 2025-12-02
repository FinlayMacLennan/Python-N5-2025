#Create a program that allows a user to:
#Enter 5 daily temperatures between -20 and +50 C
#Display all temperatures
#Calculate and display the average temperature
#Your program should use input validation, a 1-D array and fixed loops.

temps = []
total = 0
for index in range(0,5):
    tempreture = int(input("Enter todays tempreture"))
    if tempreture > -20 or tempreture < 50:
        print("Please enter a valid tempreture")
    
    elif tempreture < -20 or tempreture > 50:
        temps.append(tempreture)
#total
for x in range(len(temps)):
    total == total + temps[x]

#avarage

avarage = (total/5)

print("The total cost is:", total)