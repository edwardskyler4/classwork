import csv
I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    FILENAME = 'students.csv'
    students_dict = read_dictionary(FILENAME)

    while True:
        i_num = input("Enter the I-Number of the student you want to look up: ")
        i_num = i_num.strip().replace("-", "")

        if len(i_num) > 9:
            print ("Invalid I-Number: too many digits.")
            continue
        elif len(i_num) < 9:
            print ("Invalid I-Number: too few digits).")
            continue

        try:
            int(i_num)
        except ValueError:
            print("\nInvalid input. Try again.")
        
        break

    if i_num in students_dict.keys():
        name = students_dict[i_num]
    else:
        name = "No such student."

    print(name)

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    new_dict = {}

    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(reader)

        for line in reader:
            new_dict[line[I_NUMBER_INDEX]] = line[NAME_INDEX]

    return new_dict


if __name__ == "__main__":
    main()