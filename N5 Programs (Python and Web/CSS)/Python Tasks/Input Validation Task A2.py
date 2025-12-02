#get name from user
#get age from user
#WHILE age is less than 11 OR greater than 18
#	prompt user to try again
#	get age from user
#ENDWHILE
#display personalised message allowing user to enter talent show

#Tasks:

#Create Python code to implement the above pseudocode.

while True:

    name = input("What is your name")

    age = int(input("What is your age"))

    while age < 11 or age > 18:
        print("Please enter an age between 11 and 18")
        age = input("What is your age")
    
    print("Hello",name,"Would you like to enter the talant show?") 