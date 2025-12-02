cake = input("Is Cake Required (Yes/No)")
adults = int(input("Enter the number of adults"))
children = int(input("Enter the number of children"))
total = 0
buffet = 2


if cake == ("Yes"):
    total = total + 15
else: 
    total = total + 0

people = (adults + children)

x = int(children)

for x in range(x):
    diet = input("Please enter any dieatrty requirments for your child")

if people > 20:
    total = total + 50
else:
    total = total + 0

cost = ((buffet*children)+total)
print(cost)