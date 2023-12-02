import math
# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

try:
    radius = float(input("Enter Radius: "))
    print("Area: {}".format(math.pi*math.pow(radius, 2)))
except:
    print("Something went wrong!")