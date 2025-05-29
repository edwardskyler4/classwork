"""
This is a piece of code that takes input from a user (amount of things to be boxed and amount that can fit in a box) and tells them how many boxes they'll need.
"""

import math

def find_boxes_amount(items, fit):
    boxes = items / fit
    return boxes

while True:
    try:
        items = int(input("Items to be boxed: "))
        break
    except ValueError:
        print ("Please enter a valid input.")
        
while True:
    try:
        fit = int(input("Items that can fit in a box: "))
        break
    except ValueError:
        print ("Please enter a valid input.")

boxes = find_boxes_amount(items, fit)

print (f"If you have {items} items, with {fit} per box, you will need {math.ceil(boxes)} boxes.")