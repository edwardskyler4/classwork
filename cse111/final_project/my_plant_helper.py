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
If I just do that ^^^^, I can avoid having to use/install 5 of my 7 packages. Nice.
"""
import tkinter
import datetime
import time
import json
import threading
from personal_library import validate_int


# Use threading to have a thread that runs the timing program. 
# A function for loading, a function for saving
# A function for displaying a menu
# A function for adding plants
# A function for choosing intervals for plants, which will also start the thread for that interval
# A function to log out?


def main():
    
    menu = """
    1. Check plants and intervals
    2. Add plant
    3. Edit interval
    4. Save data
    5. Test notification
    6. Log out
"""
    user_choice = 0
    user_data = fetch_user_specific_data()

    while user_choice != 6:
        ...

    # I figure I can save the user_data as a dictionary. The key would be the username. Then I could do another dictionary for plant names and quantity, then an int or something for notification regularity.

def fetch_user_specific_data():
    """
    This function gets and returns the data of the current user. If a new user is created, it also saves that new user.
    Params: none
    Returns: user data
    """
    FILENAME = "save_plant.json"
    all_data = read_json(FILENAME)
    username = log_in(all_data)

    if username in all_data:
        user_data = all_data[username]
    else:
        all_data[username] = [{}]
        save_to_json(all_data)
        user_data = all_data[username]
    
    return user_data

def read_json(filename):
    try:
        with open(filename, "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        print ("Save file not found. Please try again.")
    return user_data

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

        if make_profile.lower in ["y", "yes"]:
            print(f"Great! Your username from now on is {username}. Don't forget it!")
        else:
            print("Okay, goodbye!")
            user_data = False

    return username

def save_to_json(user_data):
    with open("save_plant.json", "w") as f:
        json.dump(user_data)





def generate_gui():
    ...

def get_interval(notification_regularity, cur_date):
    ...

def check_date(interval, cur_date):
    ...

def send_notification():
    ...

def update_plant_info():
    ...