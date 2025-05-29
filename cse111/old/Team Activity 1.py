# import math

# while True:
#     try:
#         length = float(input ("What is the length of the pendulum in meters? "))
#         break
#     except ValueError:
#         print ("You entered an invalid input. Please try again.")

# time = (math.pi * 2) * (math.sqrt(length/9.81))

# print (f"For a pendulum with the length {length}, the time it takes to swing back and forth is {time:.2f} seconds.")


# n = int(input("What is the numeric value of n? "))

import random

n = random.randint (8, 20)

def display_matrix_1(n):
    print (f"\nMatrix Verrsion 1: n = {n}\n")

    for i in range(1, (n ** 2) + 1):
        print (f"{i:>3}", end=' ')
        if i % n == 0:
            print ()

def dispaly_matrix_2 (n):
    print (f"\nMatrix Version 2: n = {n}\n")

    for row in range(1, n + 1):
        for i in range(n):
            print (f"{row + (i * n):>3}", end=' ')
        print ()

def print_square (n):
    print()
    print ("*" * n)
    for row in range(n-2):
        print ("*", end='')
        print (' ' * (n-2), end='')
        print ("*")
    print ("*" * n)

def print_complex_square(n):
    print ()
    print ('*' * n)
    for row in range(n - 2):
        if row == 1 or row == n - 4:
            print ("* ", end='')
            print ("*" * (n - 4), end='')
            print (" *")

        elif 1 < row < n - 4:
            print ("* *", end='')
            print (" " * (n - 6), end='')
            print ("* *")

        else:
            print ("*", end='')
            print (" " * (n - 2), end='')
            print ("*")
        
    print ('*' * n)


display_matrix_1 (n)
dispaly_matrix_2 (n)
print_square (n)
print_complex_square (n)