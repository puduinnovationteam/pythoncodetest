import random

#give ruler size randomly(15,30,45)
size = random.sample(set([15 ,30 , 45]), 1)
print("Ruler size is ",size[0])

try:
    #give input number of r,g,b color boxes
    r=int(input("Enter Number of Red Boxes(1 cm) "))
    g=int(input("Enter Number of Green Boxes(5 cm) "))
    b=int(input("Enter Number of Blue Boxes(3 cm) "))

    if (r<1 or g<1 or b<1) :
        print ("Atleast each color should be prestnt once")

    else:    
        #check whether boxes cover the complete ruler
        if size[0] == r*1+g*5+b*3 :
            print("correct")
        else:
            print("wrong")
except ValueError:
    print("Sorry, enter a vaild entry")
    


