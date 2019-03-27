import random  # random module to generate a random number



def inputNumber(boxColor):
  while True:
    try:
      userInput = int(input(boxColor))
    except ValueError:
      print("Not an integer! Try again.")
      continue
    if userInput < 1:
      print("Atleast 1 box should be painted in this color");continue;
    else:
      return userInput
      break

start = input("Start Game (Y/N)?\n"); 

if(start == "Y" or start == "y"):
  while True:
    ruler = random.randint(1,3)*15;
    print("Fill the ruler of ",ruler," cm with 3 color boxes")
    red = inputNumber("Red Boxes:")*1
    blue = inputNumber("Blue boxes : ")*3
    green = inputNumber("Green boxes : ")*5
    
    if((red+blue+green) == ruler):
      print("Hurray! Correct")
    else:
      print("Oops! Wrong")

    playagain = input("Play again (Y/N)?\n")

    if(playagain =="N" or playagain == "n"):
      print("Thanks for playing!!")
      break
else:
  print("You missed it :(")
