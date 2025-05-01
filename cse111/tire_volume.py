import math
from datetime import datetime

date = datetime.now().date()

def find_volume (w, a, d):
    volume = (math.pi * w ** 2 * a * (w * a + (2540 * d))) / 10000000000
    return volume

width = float(input ("Enter the width of the tire in millimeters: "))
aspect = float(input ("Enter the aspect ratio of the tire: "))
diameter = float(input ("Enter the diameter of the wheel in inches: "))
volume = round(find_volume(width, aspect, diameter), 2)

print (f"\nThe volume of the tire is {volume} liters.")

if diameter >= 15:
    price = 115
elif diameter >= 20:
    price = 250
else:
    price = 320
tire_set = round(price * 4, 2)

print (f"\nGiven the size of the tire, a set of new tires would likely cost you around ${tire_set:.2f}.")

while True:
    want_to_buy = input ("Would you like to purchase a new set of tires? [y/n] ").lower()
    if want_to_buy in ['yes', 'y', 'no', 'n']:
        if want_to_buy in ['yes', 'y']:
            want_to_buy = 'yes'
        else:
            want_to_buy = 'no'
        break
    else:
        print ("\nYou have enterd an invalid input. Please try again.")

file = 'volumes.txt'
with open (file, "a") as f:
    print(f"{date}, {width}, {aspect}, {diameter}, {volume}, ${price}, {want_to_buy}", file=f)