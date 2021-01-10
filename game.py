import random
number=random.randint(1,10)
chances=1
while chances <5:
  guess=int(input("Enter your guess"))
  if guess == number:
      print("Congratulation YOU WON!!!")
      break
  elif guess < number: 
       print ("Your number is to low",guess)
  else:
       print ("Your number is to high",guess)
  
  chances += 1

if not chances < 5:

  print("You Lost")
