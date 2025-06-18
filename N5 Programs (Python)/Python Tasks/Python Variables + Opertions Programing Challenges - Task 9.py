#Task 9: Recipe Scaler
#Write a program that:

#Stores ingredients for a chocolate chip cookie recipe that serves 4 people 
#(flour in grams, butter in grams, sugar in grams, number of eggs, chocolate chips in grams, vanilla in teaspoons)
#Work out the scaling factor as the user wants to cook for 6 people instead
#Scale all ingredients proportionally using the calculated factor
#Display the new ingredient amounts


flour = int(input("Enter the amount of flour in grams for 4 people"))
butter = int(input("Enter the amount of butter in grams for 4 people"))
sugur = int(input("Enter the amount of sugur in grams for 4 people"))
eggs = int(input("Enter the amount of eggs for 4 people"))
chocolate = int(input("Enter the amount of chocolate in grams for 4 people"))
vanilla =int(input("Enter the amount of vanilla in teaspoons for 4 people"))

oneflour = (flour/4)
onebutter = (butter/4)
onesugur = (sugur/4)
oneeggs = (eggs/4)
onechocolate = (chocolate/4)
onevanilla = (vanilla/4)

print("Here are the new amounts of flour for 6 people", oneflour*6)
print("Here are the new amounts of butter for 6 people", onebutter*6)
print("Here are the new amounts of sugur for 6 people",onesugur*6)
print("Here are the new amounts of eggs for 6 people", oneeggs*6)
print("Here are the new amounts of chocolate for 6 people", onechocolate*6)
print("Here are the new amounts of vanilla for 6 people", onevanilla*6)