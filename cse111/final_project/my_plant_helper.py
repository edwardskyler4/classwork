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



def main():
    # collect how often user wants to be notified
    # get current date
    ...

def generate_gui():
    ...

def get_interval(notification_regularity, cur_date):
    ...

def check_date(interval, cur_date):
    ...

def send_notification():
    ...