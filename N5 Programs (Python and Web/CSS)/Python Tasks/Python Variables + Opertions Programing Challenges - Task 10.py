#Task 10: Energy Bill Calculator
#Create a program that calculates an electricity bill:

#Store that each unit costs £0.15
#Store the meter reading at the start and end of the month
#Calculate units used (i.e end reading - start reading)
#Calculate the cost of the units used
#Add a standing charge of £12 to the total cost
#Calculate and display the total bill

unit = 0.15
start = int(input("Enter the  meter reading at the start of the month"))
end = int(input("Enter the  meter reading at the end of the month"))

total = (end-start)
price = total*0.15
price = total+12

print("Your total bill for the month is £", price)