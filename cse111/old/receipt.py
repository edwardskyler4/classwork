import csv
import datetime
import random

# Indexes for products.csv
PRODUCT_CODE_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRICE_INDEX = 2

# Indexes for request.csv
PRODUCT_CODE_INDEX = 0
QUANTITY_INDEX = 1

def main():
    products_dict = read_dictionary('products.csv', PRODUCT_CODE_INDEX)
    print("---MalWart---")
    
    try:
        with open('request.csv', "rt") as f:
            reader = csv.reader(f)
            next(reader)
            subtotal = 0
            products_list = []

            for line in reader:
                product_code = line[PRODUCT_CODE_INDEX]
                quantity = int(line[QUANTITY_INDEX])

                product_name = products_dict[product_code][PRODUCT_NAME_INDEX]
                product_price = float(products_dict[product_code][PRICE_INDEX])
                cost = product_price * quantity
                subtotal += cost

                products_list.append(product_name.capitalize())
                print(f"{product_name.capitalize()}: Quantity: {quantity}, Price: {product_price}")
    except FileExistsError:
        print("\nFile not found. Please try again.")
    except KeyError:
        print(f"\nError: unknown product ID in the request.csv file '{product_code}'")
        

    print()
    print(f"Subtotal: ${subtotal:.2f}")
    tax = get_sales_tax(subtotal, 0.06)
    print(f"Tax: ${tax:.2f}")
    total = subtotal + tax
    print(f"Total: ${total:.2f}")
    print()

    print("Thank you for visiting MalWart! Have a great day!")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print()
    print()

    return_date = datetime.datetime.now() + datetime.timedelta(days = 7)
    return_date_cleaned = return_date.strftime("%Y-%m-%d")
    coupon_product = random.choice(products_list)
    print(f"Bonus! Bring this receipt back by {return_date_cleaned} to get 25% off a {coupon_product}.")


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

def get_sales_tax(subtotal, tax_rate):
    tax = subtotal * tax_rate
    return tax

if __name__ == "__main__":
    main()