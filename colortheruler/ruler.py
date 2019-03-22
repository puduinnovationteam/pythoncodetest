def make_bricks(red, blue, green, goal):
  goalval = red + (blue * 3) + (green * 5)
  #print('True') if goalval == goal else print('False')
  if (goalval == int(goal)):
    return 'Perfect'
  else:
    return 'Not Correct'

rulerList = ["","15", "30", "45"]
while True:
  try:
    rulerType = int(input("There are three rulers [1] 15cm; [2] 30cm; [3] 45cm; . Type the number displayed inside [], to select your ruler." ))
  except ValueError:
    print("Sorry, enter a vaild entry")
    continue   
  
  if rulerType > 3 or rulerType < 1:
    print("Select 1, 2 or 3")
    continue
  else:
    print("Successfully selected a ruler of ",rulerList[rulerType],"cm")    
    break

while True:
  try:
    redBoxes = int(input('Now select the number of 1cm lenth red boxes : '))
  except ValueError:
    print("Sorry, enter a valid entry")
    continue

  if redBoxes < 1:
    print('Atleast one box should be painted with Red')
    continue
  else:
    print("Painted ",redBoxes," red boxes")
    break

while True:
  try:
    blueBoxes = int(input('Now select the number of 3cm lenth blue boxes : '))
  except ValueError:
    print("Sorry, enter a valid entry")
    continue

  if blueBoxes < 1:
    print('Atleast one box should be painted with Blue')
    continue
  else:
    print("Painted ",blueBoxes," blue boxes")
    break

while True:
  try:
    greenBoxes = int(input('Now select the number of 5cm lenth green boxes : '))
  except ValueError:
    print("Sorry, enter a valid entry")
    continue

  if greenBoxes < 1:
    print('Atleast one box should be painted with Green')
    continue
  else:
    print("Painted ",greenBoxes," green boxes")
    break

#print(redBoxes,' , ',blueBoxes,' , ',greenBoxes,' , ',rulerList[rulerType])

print(make_bricks(redBoxes,blueBoxes,greenBoxes,rulerList[rulerType]))
