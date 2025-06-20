import csv

# Indexes for products.csv
PRODUCT_CODE_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRICE_INDEX = 2

# Indexes for request.csv
PRODUCT_CODE_INDEX = 0
QUANTITY_INDEX = 1

def main():
    products_dict = read_dictionary('products.csv', PRODUCT_CODE_INDEX)
    print (products_dict)
    print()

    with open('request.csv', "rt") as f:
        reader = csv.reader(f)
        next(reader)

        for line in reader:
            product_code = line[PRODUCT_CODE_INDEX]
            quantity = line[QUANTITY_INDEX]

            product_name = products_dict[product_code][PRODUCT_NAME_INDEX]
            product_price = products_dict[product_code][PRICE_INDEX]

            print(f"{product_name.capitalize()}: Quantity: {quantity}, Price: {product_price}")
            


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(reader)

        for line in reader:
            dictionary[line[key_column_index]] = line
    
    return dictionary


if __name__ == "__main__":
    main()