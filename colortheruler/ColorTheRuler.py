import random as randomRulerSize


def IsRulerColoredFully(rulerSize):
	isColored = True
	while True:
		redBoxCount = input("\n enter the number of red boxes....\n")
		try:
			redCount = int(redBoxCount)
			break
		except ValueError:
			print("Enter proper integer Value")
	while True:
		blueBoxCount = input("\n enter number of blue boxes\n")
		try:
			blueCount = int(blueBoxCount)
			break
		except ValueError:
			print("Enter proper integer Value")
	while True:
		greenBoxCount = input("\n enter the number of green boxes \n")
		try:
			greenCount = int(greenBoxCount)
			break
		except ValueError:
			print("Enter proper integer Value")
	if ((redCount*1)+(blueCount*3)+(greenCount*5))==rulerSize:
		isColored = True
	else:
		isColored = False
	return isColored



print("\n Color the Ruler....!!!!")
RulerSizelist = [15,30,45]
PreviousRulers = [] 
ExitValue = False
print("\n The ruler sizes are....\n",RulerSizelist)
while True:
	if ExitValue == True:
		break
	ruler = randomRulerSize.choice(RulerSizelist)
	if ruler not in PreviousRulers:
		if len(PreviousRulers)==(len(RulerSizelist)-1):
			PreviousRulers.clear()
		PreviousRulers.append(ruler)
		print("\n Color the scale provided...:)))")
		print("\n",ruler)
		if IsRulerColoredFully(ruler) == True:
			print("\n The ruler has been colored \n ")
			while True:
				value = input("Do you want to Exit? press 'Y' for yes or 'N' for No ....")
				if value == "Y" or value == "y":
					ExitValue = True
					break
				elif value == "n" or value == "N":
					break
				else:
					print("\n Enter proper value")			
	
		

	
	


