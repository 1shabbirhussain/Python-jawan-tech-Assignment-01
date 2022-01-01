print ("Twinkle Twinkle Little star, \n    How I Wonder What you Are! \n       Up Above the world so high \n       Like the diamond In the Sky \nTwinkle Twinkle Little star \n     How I wonder what you are");

import sys
print("Python version"+ sys.version );
print(f"Version info {sys.version_info}")

import datetime
now = datetime.datetime.now()
print (f'current date and time is: {now}' )

import math
r = eval(input("input radius: "))
x = math.pi * (r*r)
y=round(x,2)
print(f"Area of a circle is {y}")


fname = input("enter first name:");'\n'
lname = input("enter last name:"); '\n'
print(lname +" "+ fname);

finput = eval(input("enter first input: "));
sinput = eval(input("enter second input: "));
c = finput+ sinput;
print(f"sum is {c}")
