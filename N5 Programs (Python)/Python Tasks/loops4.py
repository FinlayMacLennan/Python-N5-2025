# Program 4 - Investigate and modify

rightnumber = 8
guess = 1
number = int(input("Guess a number: "))

while (guess < 5) and (number != rightnumber):
  print("Not right. Try again.")
  number = int(input("Guess a number: "))
  guess = guess + 1
    if number == rightnumber
        print("Well done!")