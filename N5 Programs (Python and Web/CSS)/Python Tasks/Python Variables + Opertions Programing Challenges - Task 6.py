#Task 6: Exam Results
#Create a program that:

#Stores an overall mark for each of 4 different subjects (e.g. English, Maths, Computing, Art & Design)
#Calculates the sum total of all marks entered by the user
#Calculates the average mark
#Displays all results with appropriate labels

English = int(input("What was your total mark for English"))
Maths = int(input("What was your total mark for Maths"))
Computing = int(input("What was your total mark for Computing"))
Art = int(input("What was your total mark for Art"))

Totalmarks = (English+Maths+Computing+Art)

avgmark = (Totalmarks/4)

print("Your total amount of marks is", Totalmarks)
print("Your Avarage mark is", avgmark)
