import random  # random module to generate a random number

start = input("Start Game (Y/N)?"); 

if(start == "Y"):
  while True:
    ruler = random.randint(1,3)*15;
    print("Fill the ruler of ",ruler," cm with 3 color boxes")
    while True:
      try:
        red = int(input("Red boxes :"))*1
      except ValueError:
        print("Enter a valid entry!")
        continue;
      if red < 1:
        print("Atleast 1 red box should be painted")
        continue;
      else:
        break;
    while True:
      try:
        blue = int(input("Blue boxes : "))*3
      except ValueError:
        print("Enter a valid entry!")
        continue;
      if blue < 1:
        print("Atleast 1 blue box should be painted")
      else:
        break;
    while True:
      try:
        green = int(input("Green boxes : "))*5
      except ValueError:
        print("Enter a valid entry!")
        continue;
      if green < 1:
        print("Atleast 1 blue box should be painted")
      else:
        break;
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