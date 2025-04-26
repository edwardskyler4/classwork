import math

def find_volume (w, a, d):
    volume = (math.pi * w ** 2 * a * (w * a + (2540 * d))) / 10000000000
    return volume

width = float(input ("Enter the width of the tire in millimeters: "))
aspect = float(input ("Enter the aspect ratio of the tire: "))
diameter = float(input ("Enter the diameter of the wheel in inches: "))

print (f"The volume of the tire is {find_volume(width, aspect, diameter):.2f} liters.")