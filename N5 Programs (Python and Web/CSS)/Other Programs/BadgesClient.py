#Badges

badges = int(input("How many badges do you want to order"))

if badges < 150:
	price = (badges*0.25)

else:
	price = (badges*0.25*0.9)
	
print("Your total order comes to","£",price)