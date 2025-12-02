#Task 7: Library Fine Calculator
#Write a program that:

#Stores the number of days a book is overdue
#The fine is £0.50 per day
#If the fine exceeds £5, add an additional £2 processing fee
#Calculate and display the total fine


days = int(input("How many days is your book overdue?"))

fine = (days * 0.50)

if fine > 5:
    fine = (fine + 2)

else:
    fine = fine + 0

print(fine)