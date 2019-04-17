import random
import string


password = ""
characters = ""
category = ""
passwordSize = 0;

def validateInput(category):
  global characters
  global password
  global passwordSize
  condition = True
  character = ""
  if category == 'upperCase':
    character = string.ascii_uppercase
  elif category == 'digits':
    character = string.digits
  else:
    character  = string.punctuation;

  while condition:
    userInput = input("")
  
    if(userInput == 'Y' or userInput == 'y' or userInput == 'N' or userInput == 'n' ):
      if(userInput == 'Y'or userInput == 'y'):
        password += random.choice(character)
        passwordSize = passwordSize - 1
        characters += character
        condition = False  
      if(userInput == 'N'or userInput == 'n'):
        condition = False
    else:
      print("Please respond with Y or N ")



print("\n*******Password Generator*******\n")
print("Please answer the following questions to generate a password!\n")


while True:
  print("\n1. Please enter the length of your password:")
  try:
    passwordSize = int(input(""))

    if(passwordSize<8):
      print("Recommended minimum password length is 8")
      continue
    if(passwordSize>20):
      print("Recommended maximum password length is 20")
      continue
    elif(passwordSize<1):
      print("Enter a value greater than 0!!")
      continue
    break
  except ValueError:
    print("Please try again with a number!!")

print("\n3. Do you want to include upper-case letters in your password? (Y/N)")
category = "upperCase"
validateInput(category)


print("\n4. Do you want to include digits in your password? (Y/N)")
category = "digits"

validateInput(category)

print("\n5. Do you want to include special characters in your password? (Y/N)")
category = "specialCharacters"

validateInput(category)

for i in range(passwordSize):
  password += random.choice(characters+string.ascii_lowercase)

print("\nThe length of the password is " , passwordSize, " and the generated password is "+ password)