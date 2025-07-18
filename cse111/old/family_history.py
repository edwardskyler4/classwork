# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1695, 1752],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1737, 1803],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1802, 1858],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1899, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1829],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    # print_death_age(people_dict)

    # Print a blank line.
    # print()

    # Call the count_genders function to count
    # and print the number of males and females.
    # count_genders(people_dict)

    # Print a blank line.
    # print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    # print_marriages(marriages_dict, people_dict)

    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Death Information:")
    for person_keys in people_dict:
        name = people_dict[person_keys][NAME_INDEX]
        birth_year = int(people_dict[person_keys][BIRTH_YEAR_INDEX])
        death_year = int(people_dict[person_keys][DEATH_YEAR_INDEX])
        death_age = death_year - birth_year
    
        print(f"Name: {name}")
        print(f"Birth Year: {birth_year}")
        print(f"Death Year: {death_year}")
        print(f"Age at death: {death_age}")
        print()


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    m_count = 0
    f_count = 0

    for person_keys in people_dict:
        gender = people_dict[person_keys][GENDER_INDEX]
        if gender == "M":
            m_count += 1
        else:
            f_count += 1

    print()
    print("Gender Information:")
    print(f"Total females: {f_count}")
    print(f"Total males: {m_count}")
    print()


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print()
    print("Marriage Information:")
    
    for marriage_key in marriages_dict:
        wedding_year = int(marriages_dict[marriage_key][WEDDING_YEAR_INDEX])

        h_key = marriages_dict[marriage_key][HUSBAND_KEY_INDEX]
        w_key = marriages_dict[marriage_key][WIFE_KEY_INDEX]

        h_name = people_dict[h_key][NAME_INDEX]
        h_age = wedding_year - int(people_dict[h_key][BIRTH_YEAR_INDEX])

        w_name = people_dict[w_key][NAME_INDEX]
        w_age = wedding_year - int(people_dict[w_key][BIRTH_YEAR_INDEX])

        print(f"{h_name} ({h_age}) married {w_name} ({w_age}) in {wedding_year}.")


def count_marriages(marriages_dict, people_dict):
    marriage_count = {}

    for marriage_key in marriages_dict:
        h_key = marriages_dict[marriage_key][HUSBAND_KEY_INDEX]
        h_name = people_dict[h_key][NAME_INDEX]

        w_key = marriages_dict[marriage_key][WIFE_KEY_INDEX]
        w_name = people_dict[w_key][NAME_INDEX]

        # For some reason the code doesn't count right if I put them in by name instead of by key
        if h_key in marriage_count:
            marriage_count[h_key] += 1
        else:
            marriage_count[h_key] = 1
        
        if w_key in marriage_count:
            marriage_count[w_key] += 1
        else:
            marriage_count[w_key] = 1


    for key, item in marriage_count.items():
        name = people_dict[key][NAME_INDEX]
        print (f"{name}: {item}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
