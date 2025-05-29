def main():
    '''
    Calculates a user's fuel efficiency.
    Arguments accepted: none
    Return: Prints out the user's miles per gallon and litres per 100km.
    '''
    odont_start = input ("\nEnter starting odometer reading (miles): ")
    odont_start = float(validate_as_float (user_input=odont_start))

    odont_end = input ("Enter ending odometer reading (miles): ")
    odont_end = float(validate_as_float (user_input=odont_end))

    fuel_use = input ("Amount of fuel used (gallons): ")
    fuel_use = float(validate_as_float(user_input=fuel_use))

    mpg = calculate_miles_per_gallon(odont_start, odont_end, fuel_use)
    lp100k = calculate_lp100k_from_mpg(mpg)

    print (f"\nMiles Per Gallon: {mpg:.2f} \nLitres Per 100 Kilometers: {lp100k:.2f}")

def validate_as_float(user_input):
    '''
    Validates the user's input as a float.
    Arguments accepted: a user's input to a prompt designed to collect float information
    Return: user input formatted as a float
    '''
    while True: # I could make this cleaner by making each of the user info collection as its own function, meaning I could feed it into this function as a argument, which means I could ask the question again instead of just telling the user to try again.
        try:
            float(user_input)
            break
        except ValueError:
            user_input = input("\nYou have entered an invalid input. Please try again: ")
    return user_input
    
def calculate_miles_per_gallon(start_miles, end_miles, gallons):
    '''
    Calculates miles per gallon
    Arguments: starting odometer reading, ending odometer reading, gallons of fuel used in that journey
    Return: miles per gallon
    '''
    mpg = abs(end_miles - start_miles) / gallons
    return mpg

def calculate_lp100k_from_mpg(mpg):
    '''
    Calculates litres per 100 kilometers (lp100k) from mpg.
    Arguments: mpg (miles per gallon)
    Return: lp100k
    '''
    lp100k = 235.215 / mpg
    return lp100k


main()