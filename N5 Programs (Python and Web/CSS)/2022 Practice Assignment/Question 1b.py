# Qestion 1b - 15 Marks

totalWeight = 0
FoodWeight2 = []
for index in range(5):
    FoodWeight = float(input("Please enter the food weight for each container"))
    while FoodWeight < 0 or FoodWeight > 200:
        print("Invaild, a single container can only hold up to 200g")
        FoodWeight = int(input("Please enter the food weight for each container"))
    totalWeight = totalWeight + FoodWeight
    FoodWeight2.append(FoodWeight)

DogSize = input("Please enter the size of your dog: small, medium or large")

if DogSize == "small" and totalWeight > 110 and totalWeight < 140:
    recomened_message = "This weight of food is sutable for your small dog"
elif DogSize == "medium" and totalWeight > 330 and totalWeight < 440:
    recomened_message = "This weight of food is sutable for your medium dog"
elif DogSize == "large" and totalWeight > 690 and totalWeight < 900:
    recomened_message = "This weight of food is sutable for your large dog"
else:
    recomened_message = "This weight of food is not recommened for the size of dog"

avergeWeight = totalWeight/5
avergeWeight = round(avergeWeight,1)

for index in range(5):
    print(FoodWeight2[index])
print(totalWeight)
print(avergeWeight)
print(recomened_message)