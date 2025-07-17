"""
My Plant Helper
This program is designed to remind the user when to water their plants. It's going to do a couple of things:
1. Generate a GUI
2. Ask the user how often they want to be reminded to water their plants
3. Get the current date
4. Find the interval of time at the end of which the user wants to be notified
5. Continue to check the date every 24 hours until the interval is reached
6. Send a notification to the user's desktop telling them to water their plants

Stretch goals:
1. Get the user's name. Personalize the messaging
2. Let them continue to change their settings as often as they want
3. Let them input multiple plants and intervals
4. Send notifications to the phone rather than the computer

Other notes:
I need to be able to save and load data, which I can do with a JSON.
If I do the JSON, I can pretty easily save the user's data.
I can use time.sleep to make my own kind of cron job
I could get the time of day that the user wants to be notified and use datetime to keep checking until it's that time of the appropriate day
I can do a basic notification by just printing it to the terminal.
"""
import tkinter
import datetime
import time
import json
import threading


# Use threading to have a thread that runs the timing program. 
# A function for loading, a function for saving
# A function to edit plants and intervals
# A function for adding plants
# A function for choosing intervals for plants, which will also start the thread for that interval
# A function to log out?


def main():
    PLANT_NAME_INDEX = 0
    QUANTITY_INDEX = 1
    WATER_FREQUENCY_INDEX = 2
    MENU = """
    1. Check plants and intervals
    2. Add plant
    3. Edit plant
    4. Save data
    5. Test notification
    6. Log out
"""
    FILENAME = "save_plant.json"

    user_choice = 0
    has_saved = False

    all_data = read_json(FILENAME)
    username = log_in(all_data)

    if username != False:
        if username in all_data:
            user_data = all_data[username]
        else:
            all_data[username] = {}
            save_to_json(all_data)
            user_data = all_data[username]
    else:
        user_data = False

    run = False if user_data == False else True

    if run == True:
        print("\nWelcome! Please look at the below menu and type a number to choose that option.")

    while run == True:
        print(MENU)
        user_choice = input("Enter your choice: ")

        if user_choice not in str(list(range(1, 7))):
            print("\nYou have entered a number outside of the provided menu options. Please try again.")
            continue
        

        if user_choice == "1": # check plants and intervals # technically works, but not done
            print(user_data) # add more logic for printing to make it prettier
        
        elif user_choice == "2": # Add plant # seems to work. Haven't yet tested fully.
            plant_run = True
            while plant_run == True:
                plant_name = input("Name of your plant: ")

                plant_quantity = input(f"Quantity of {plant_name}: ")

                interval_choice = input(f"""When to get watering reminders for {plant_name}:
                                    1. Every week
                                    2. Every two weeks
                                    3. Every three weeks
                                    4. Every month
                                    5. Every two months
                                    6. Cancel
                                    Your choice: """)
                
                if interval_choice not in str(list(range(1, 7))):
                    print("\nYou have entered a number outside of the provided menu options. Please try again.")
                
                if interval_choice == "1":
                    water_interval = "weekly"

                elif interval_choice == "2":
                    water_interval = "bi-weekly"
                
                elif interval_choice == "3":
                    water_interval = "tri-weekly"
                
                elif interval_choice == "4":
                    water_interval = "monthly"
                
                elif interval_choice == "5":
                    water_interval = "bi-monthly"
                
                elif interval_choice == "6":
                    plant_run = False
                    break

                user_data[plant_name] = [plant_name, plant_quantity, water_interval]
                has_saved = False

                print (f"You have sucessfuly added {user_data[plant_name][PLANT_NAME_INDEX]}, \nwith a quantity of {user_data[plant_name][QUANTITY_INDEX]},\nbeing watered on a {user_data[plant_name][WATER_FREQUENCY_INDEX]} schedule.")

                add_another = input("Would you like to add another plant? (y/n) ")

                if add_another.lower() in ["y", "yes"]:
                    plant_run = True
                else:
                    print("\nOkay. Please select an option from the menu options below:")
                    plant_run = False

        elif user_choice == "3": # edit plant
            ...

        elif user_choice == "4": # Save data # finished writing, have tested a bit
            all_data[username] = user_data
            save_to_json(all_data)
            print("\nSuccessfully saved.")
            has_saved = True
        
        elif user_choice == "5": # Test notification
            ...

        elif user_choice == "6": # log out # finished writing, haven't yet tested at all
            if has_saved == False:
                confirm_save = input("You haven't saved your changes. Are you sure you'd like to quit? (y/n) ")

                if confirm_save.lower() in ["y", "yes"]:
                    run = False
                    print("\nGoodbye!")
                else:
                    pass
            else:
                run = False
                print ("\nGoodbye!")


    
def read_json(filename):
    try:
        with open(filename, "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        print ("Save file not found. Please try again.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        user_data = {}
    return user_data

def save_to_json(user_data):
    with open("save_plant.json", "w") as f:
        json.dump(user_data, f, indent=4)

def log_in(user_data):
    """
    Function: log_in
    This function gets a username from a user, then checks if it's in a dictionary of user data. If it is, it returns the username. If it isn't, it prompts the user to create a new, unique username.
    Params: the dictionary of user data
    Returns: the username of the user, or False if they decide to not create a username.
    """
    username = input("What is your username? ")

    if username not in user_data:
        make_profile = input("It looks like we don't have you in our system. Would you like to create a profile? (y/n) ")

        if make_profile.lower() in ["y", "yes"]:
            print(f"\nGreat! Your username from now on is '{username}'. Don't forget it!")
        else:
            print("\nOkay, goodbye!")
            username = False

    return username

def start_notification_interval(interval): # I need to figure out how I could have multiple timers running at the same time. Also need to learn how thread works.
    """
    This function is going to start a thread that will send a notification at the specified interval (date) at 12:00pm MST (or the user's timezone). To set up multiple notifications, you'll need to call this function multiple times.
    """
    ...



if __name__ == "__main__":
    main()