'''
This is a calculator that will be able to determine the area of circles and triangles.
The user will select a shape and the calculator will calculate the area of the shape selected.
'''

from math import pi
from datetime import datetime

now = datetime.now()

print ("The calculator is starting up...")

print ('%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))

hint = "Don't forget to include the correct units!"

option = input("Enter C for Circle or T for Triangle: ")

if option.lower() == 'c':
    radius = float(input("What's the radius of your circle?"))
    circarea = pi * radius ** 2
    print ("The area of a circle with a radius of %s is %s" % (radius, circarea))

elif option.lower() == 't':
    height = float(input("What's the height of your triangle?"))
    base = float(input("What's the length of the base of your triangle?"))
    triarea = height * base / 2
    print ("The area of a triangle with a height of %s and a base that is %s long is %s" % (height, base, triarea))
else:
    print ("You chose neither a circle nor a triangle.")
    print ("Shutting down...")
