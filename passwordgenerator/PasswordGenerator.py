import random
import string

def GeneratePassowd(uppercaseLen,lowercaseLen,numbersLen, splcharsLen):
	password = []	
	if uppercaseLen > 0:
		for i in range(0,uppercaseLen):
			value = random.choice(string.ascii_uppercase)
			if value not in password:
				password.append(value)
			else:
				i = i-1
	if lowercaseLen > 0:
		for i in range(0,lowercaseLen):
			value = random.choice(string.ascii_lowercase)
			if value not in password:
				password.append(value)
			else:
				i = i-1
	if numbersLen > 0:
		for i in range(0,numbersLen):
			value = random.choice(string.digits)
			if value not in password:
				password.append(value)
			else:
				i = i-1
	if splcharsLen > 0:
		for i in range(0,splcharsLen):
			value = random.choice(string.punctuation)
			if value not in password:
				password.append(value)
			else:
				i = i-1
	random.shuffle(password)
	return ''.join(password)


print("\n \t\t\t Welcome to Password Generator....!!!:::))))")
isExit = False
Password = ''
while True:
	PasswordLen = 0
	uppercaseLen = 0
	lowercaseLen = 0
	DigitsLen = 0
	SplCharLen = 0
	count = 0
	if isExit == True:
		print("\n Thank you for using Password Generator")
		break
	while True:
		try:
			PasswordLen = int(input("\n Enter the length of the password \t"))
		except(ValueError):
			print("\n enter an digit")
		if PasswordLen > 10 and PasswordLen < 20 :
			print("\n Password length is in good size")
			break
		elif PasswordLen > 20:
			print("\n Password length is too long")
		else: 
			print("\n Password Length is too small")
	while True:
		try:
			uppercaseLen = int(input("\n Enter the length of the uppercaseLen \t"))
		except(ValueError):
			print("\n enter an digit")
		
		if uppercaseLen > PasswordLen:
			print("\n Give Valid Length of Uppercase")
		else:
			if uppercaseLen != 0:
				count = count +1
			break
	while True:
		try:
			lowercaseLen = int(input("\n Enter the length of the LowerCase \t"))
		except(ValueError):
			print("\n enter an digit")
		if (uppercaseLen+lowercaseLen) > PasswordLen:
			print("\n Give Valid Length of Lower Case")
		else:
			if uppercaseLen != 0:
				count = count +1
			break
	while True:
		try:
			DigitsLen = int(input("\n Enter the length of the Digits\t"))
		except(ValueError):
			print("\n enter an digit")
		if (uppercaseLen+lowercaseLen+DigitsLen) > PasswordLen:
			print("\n Give Valid Length of Digits")
		else:
			if uppercaseLen != 0:
				count = count +1
			break
	while True:
		try:
			SplCharLen = int(input("\n Enter the length of the Special Character\t"))
		except(ValueError):
			print("\n enter an digit")
		if (uppercaseLen+lowercaseLen+DigitsLen+SplCharLen) > PasswordLen:
			print("\n Give Valid Length of Special Character")
		else:
			if uppercaseLen != 0:
				count = count +1
			break
	if count == 1:
		print("\n your password strenght is weak")
	elif count == 2 :
		print (" \n your password strenght is weak")
	elif count == 3:
		print ("\n your password strenght is normal")
	elif count == 4:
		print("\n your password strenght is very strong ")
	Password = GeneratePassowd(uppercaseLen,lowercaseLen,DigitsLen,SplCharLen)
	print("\n Your Password is ....", Password)
	while True:
		value = input("\n Do you want to exit..Press 'Y' for Yes or 'N' for No ....\t")
		if value == 'y' or value =='Y':
			isExit = True
			break
		elif value == 'N' or value == 'n':
			break
		else:
			print ("\nEnter proper value..") 
			
