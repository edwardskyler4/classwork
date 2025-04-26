"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("Please enter your age: "))

max_hr = 220 - age
range_top = max_hr * 0.85
range_bottom = max_hr * 0.65

print (f"When you exercise to strengthen your heart, you should keep your heart rate between {int(range_bottom)} and {int(range_top)} beats per minute.")