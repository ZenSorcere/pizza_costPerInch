# pizza_cost.py
# calculate the cost per square inch of a circular pizza

# Import math library
from math import *


def main ():
# Inform user of program purpose.   
    print("This program calculates the price per square inch of a pizza. \n")

# Get size of pizza, and divide by 2 to get radius (pizza sizes are
#   always the diameter). Then calculate the area of a circle. 
    diameter = int(input("Enter the pizza size (in inches): "))
    radius = diameter / 2
    area = pi * (radius**2)

# get cost of pizza in dollars and cents (as seen on a menu). 
    cost = float(input("Enter the cost of the pizza (in dollars & cents): "))

# take price of pizza, multiply by 100 to get raw cents, then
#   divid by the area to get cost/inch.
    inchCost = (cost*100) / area

# Round the value of "inchCost" to second decimal place, and output answer.
    print("The cost is", round(inchCost, 2), "cents per square inch.")

main()
