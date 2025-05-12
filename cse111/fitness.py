# weight in kilos, height in centimeters



# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def test_if_float(statement):
    while True:
        try:
            float(statement)
            break
        except ValueError:
            ...
# In progress ^^^^^

def get_weight():
    weight_str = input ("Enter your weight. Ex: 123 lbs, 454 kg, etc.: ")
    # Uncompleted here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def main():
    gender = input("Input your gender (M/F): ")
    birth_str = input("Input your birthdate (YYYY-MM-DD. Include leading zeros): ")
    weight = int(input("Input your weight in pounds: "))
    height = int(input("Input your height in inches: "))

    age = compute_age(birth_str=birth_str)
    height_cm = cm_from_in(inches=height)
    weight_kg = kg_from_lb(pounds=weight)

    bmi = body_mass_index(weight=weight_kg, height=height_cm)
    bmr = basal_metabolic_rate(gender=gender, weight=weight_kg, height=height_cm, age=age)

    print (f"\nAge: {age}")
    print (f"Weight: {weight_kg:.2f} kg")
    print (f"Height: {height_cm:.2f} cm")
    print (f"Body Mass Index (BMI): {bmi:.2f}")
    print (f"Basal Metabolic Rate (BMR): {bmr:.2f}")

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kilograms = pounds / 2.205
    return kilograms


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    centimeters = inches * 2.54
    return centimeters



def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * weight / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

    return bmr


# Call the main function so that
# this program will start executing.

main()
