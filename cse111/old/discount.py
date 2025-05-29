from datetime import datetime

def is_deal(subtotal):
    """
    Checks to see if the 10% deal needs to be applied or not. 
    Math could be added into the function as well if you wanted to.
    """
    today = datetime.now()
    day_of_week = today.weekday()
    if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
        return True
    else:
        return False

while True:
    try:
        subtotal = input("Enter your subtotal: ").replace("$", "")
        subtotal = float(subtotal)
        break
    except ValueError:
        print ("You have entered an invalid input. Please try again.")


if is_deal(subtotal):
    subtotal_with_deal = subtotal * 0.9
    tax = subtotal_with_deal * 0.06
    total = subtotal_with_deal + tax
    print (f"\nSubtotal after applying 10% discount: ${subtotal_with_deal:.2f}\nSales tax: ${tax:.2f}\nTotal: ${total:.2f}")
else:
    tax = subtotal * 0.06
    total = subtotal + tax
    print (f"\nSales tax: ${tax:.2f} \nTotal: ${total}")