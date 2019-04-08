import random
import string

password = ""
characters = ""

print("\n*******Password Generator*******\n")
print("Please answer the following questions to generate a password!\n")

print("1. Please enter the minimum length of your password:")
while True:
  try:
    passwordMinSize = int(input(""))
    if(passwordMinSize<1):
      print("Enter a value greater than 0!!")
      continue
    break
  except ValueError:
    print("Please try again with a number!!")

print("\n2. Please enter the maximum length of your password:")
while True:
  try:
    passwordMaxSize = int (input(""))
    if(passwordMaxSize<passwordMinSize):
      print("Enter a value greater than the minimum length!!")
      continue
    break
  except ValueError:
    print("Please try again with a number!!")

print("\n3. Do you want to include upper-case letters in your password? (Y/N)")
while True:
  upperCaseLetters = input("")

  if(upperCaseLetters == 'Y' or upperCaseLetters == 'y' or upperCaseLetters == 'N' or upperCaseLetters == 'n' ):

    if(upperCaseLetters == 'Y'or upperCaseLetters == 'y'):
      characters += string.ascii_uppercase
      break
    if(upperCaseLetters == 'N'or upperCaseLetters == 'n'):
      break
  else:
    print("Please respond with Y or N ")

print("\n4. Do you want to include lower-case letters in your password? (Y/N)")
while True:
  lowerCaseLetters = input("")

  if(lowerCaseLetters == 'Y' or lowerCaseLetters == 'y' or lowerCaseLetters == 'N' or lowerCaseLetters == 'n' ):

    if(lowerCaseLetters == 'Y'or lowerCaseLetters == 'y'):
      characters += string.ascii_lowercase
      break
    if(lowerCaseLetters == 'N'or lowerCaseLetters == 'n'):
        break

  else:
    print("Please respond with Y or N ")

print("\n5. Do you want to include digits in your password? (Y/N)")
while True:
  digits = input("")

  if(digits == 'Y' or digits == 'y' or digits == 'N' or digits == 'n' ):

    if(digits == 'Y'or digits == 'y'):
      characters += string.digits
      break
    if(digits == 'N'or digits == 'n'):
      break    

  else:
    print("Please respond with Y or N ")

print("\n6. Do you want to include special characters in your password? (Y/N)")
while True:
  specialCharacters = input("")

  if(specialCharacters == 'Y' or specialCharacters == 'y' or specialCharacters == 'N' or specialCharacters == 'n' ):

    if(specialCharacters == 'Y'or specialCharacters == 'y'):
      characters += string.punctuation
      break
    if(specialCharacters == 'N'or specialCharacters == 'n'):
      break    

  else:
    print("Please respond with Y or N ")

print("\n7. Do you want to include white space in your password? (Y/N)")
while True:
  whiteSpace = input("")

  if(whiteSpace == 'Y' or whiteSpace == 'y' or whiteSpace == 'N' or whiteSpace == 'n' ):

    if(whiteSpace == 'Y'or whiteSpace == 'y'):
      characters += string.whitespace
      break
    if(whiteSpace == 'N'or whiteSpace == 'n'):
      break    

  else:
    print("Please respond with Y or N ")

passwordSize = random.randint(passwordMinSize,passwordMaxSize)

for i in range(passwordSize):
        password += random.choice(characters)

print("\nThe length of the password is " , passwordSize, " and the generated password is "+ password)