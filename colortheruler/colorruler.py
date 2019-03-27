import random

#give ruler size randomly(15,30,45)
size = random.sample(set([15 ,30 , 45]), 1)
print("Ruler size is ",size[0])

def getinput():
        while True:
            try:
                temp = int(input())
                if (temp > 0):
                  break
                else:
                  print ("Sorry, Atleast each color should be prestnt once. Enter number of boxes again")
                  continue
            except ValueError:
                print("Sorry, only integers are allowed. Enter number of boxes again")
                continue
        return temp

while True:

    #give input number of r,g,b color boxes
    print("Enter Number of RedBoxes ")
    r=getinput()
    print("Enter Number of GreenBoxes ")
    g=getinput()
    print("Enter Number of BlueBoxes ")
    b=getinput()

    #check whether boxes cover the complete ruler
    if size[0] == r*1+g*5+b*3 :
      print("correct")
    else:
      print("wrong")
      
    break
