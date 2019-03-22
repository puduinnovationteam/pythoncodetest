import random  # random module to generate a random number

start = input("Start Game (Y/N)?"); 

if(start == "Y"):
  while True:
    ruler = random.randint(1,3)*15;
    print("Fill the ruler of ",ruler," cm with 3 color boxes")
    red = int(input("Red boxes :"))*1
    blue = int(input("Blue boxes : "))*3
    green = int(input("Green boxes : "))*5

    if((red+blue+green) == ruler):
      print("Hurray! Correct")
    else:
      print("Oops! Wrong")
    
    playagain = input("Play again (Y/N)?")

    if(playagain =="N"):
      print("Thanks for playing!!")
      break

else:
  print("You missed it :(")   