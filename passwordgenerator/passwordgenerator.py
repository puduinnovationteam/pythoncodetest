import random
import string
from random import *

#inputs
while True:
	try:
		pwdlen = int(input('Enter Length of the password(Min chars is 4)'))
		if pwdlen >= 4 :
			print(pwdlen)
			break
		else :
			print('Min length should be 4')
			continue
	except ValueError:
		print("Sorry, only integers are allowed. Enter password length again")
		continue
keyword = input('Enter a keyword(keyword can contains lower case , upper case and special characters)')

#password generation		
characters = keyword + string.digits 
count = 0
password=""
while count != pwdlen:
	password += choice(characters)  	  
	count+=1	
	continue

#print password
print(password)





