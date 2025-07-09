def validate_int(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("\nInvalid input. Please try again.")

        if user_input > max_value:
            print(f"{user_input} is an invalid input. Enter a lower number.")
            continue
        elif user_input < min_value:
            print(f"{user_input} is an invalid input. Enter a higher number.")
            continue
        else:
            break
    
    return user_input

def validate_float(prompt, min_value, max_value):
    while True:
        try:
            user_input = float(input(prompt))
        except ValueError:
            print("\nInvalid input. Please try again.")

        if user_input > max_value:
            print(f"{user_input} is an invalid input. Enter a lower number.")
            continue
        elif user_input < min_value:
            print(f"{user_input} is an invalid input. Enter a higher number.")
            continue
        else:
            break
    
    return user_input




