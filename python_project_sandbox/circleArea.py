#import math module and fx
from math import pi

#user: what is circle radius?
r = float(input("what is circle radius: "))

# make sure this is right
print("you wrote "+str(r)+" - is that right?")

a = input(" y or n ")
if a == "y":
    area = pi * r **2
    print("The area is "+str(area) + "!")
elif a == "n":
   print("oops")
else:
    print("okay")
