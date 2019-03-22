import random

#give ruler size randomly(15,30,45)
size = random.sample(set([15 ,30 , 45]), 1)
print("Ruler size is ",size[0])

#give input number of r,g,b color boxes
r=int(input("Enter Number of Red Boxes "))
g=int(input("Enter Number of Green Boxes "))
b=int(input("Enter Number of Blue Boxes "))

#check whether boxes cover the complete ruler
if size[0] == r*1+g*5+b*3 :
    print("correct");
else:
    print("wrong");
