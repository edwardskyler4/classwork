"""
Auth: Dream Team
Date: 05/14/2025
IDE: VS Code
Deesc: Compute can efficiency and order
"""
import math

def main():
    cans = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall",	7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32,	11.91, 0.61],
        ["#3 Cylinder",	10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

#    for i in range(len(cans)):
    for i in range(1):
        name = cans[i][0]
        radius = cans[i][1]
        height = cans[i][2]
        cost = cans[i][3]

        volume = compute_volume(radius, height)
        print(volume)
        surface_area = compute_surface_area(radius, height)
        print(surface_area)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)

        print (f"Item: {name}\nStorage Efficiency: {storage_efficiency}")


def compute_storage_efficiency(volume, surface_area):
    """
    Compute the storage efficieny
    Parameters: Volume, Surface Area
    Returns Storage Efficiency
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency


def compute_volume(radius, height):
    """
    Compute the volume of the can
    Parameters: radius, height
    Returns Volume
    """
    volume = math.pi * (radius ** 2) * height
    return volume
    
def compute_surface_area(radius, height):
    """
    Computes the surface area of a cylinder
    Parameters: radius, height
    Return: surface area
    """
    surface_area = 2 * math.pi * radius * (radius * height)
    return surface_area

main()