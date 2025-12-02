#Task 5: Pizza Party Calculator
#Write a program that:

#Stores the number of students in the class
#Stores that each pizza serves 8 people
#Calculate how many pizzas are needed (you may need to round up)
#If each pizza costs £12, calculate the total cost
#Display the number of pizzas needed and the total cost

students = int(input("How meny studants are there?(Rounded to the nerest 8)"))

pizza = 8

numberofpizzas = (students/pizza)

cost = numberofpizzas*12

print(numberofpizzas)
print("The total cost is £", cost)