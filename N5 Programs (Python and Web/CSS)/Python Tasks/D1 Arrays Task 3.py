#How can we change the program so that it asks for and stores 3 full names in the name array?

# Program 3 - Investigate and Modify
import random

price = [random.randint(1,100) for index in range(100)]
total = 0
for x in range(len(price)):
    total == total + price[x]
print('The total cost is: £' + str(total))
print(price)