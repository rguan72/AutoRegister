# coding=utf-8
import sys, os, time, subprocess, getpass
from datetime import datetime, timedelta
import pytz
from constants import EST
from selenium import webdriver
from navHelper import NavHelper

# Main menu
def main_menu():

    while True:
        os.system("cls" if sys.platform == "win32" else "clear")
        print("Welcome to AutoRegister!")
        print("Please choose the menu you wish to start")
        print("1. Run Now")
        print("2. Run Later")
        print("3. Get Cookies")
        print("\n0. Quit")
        choice = input(">> ")
        exec_menu(choice)
        time.sleep(2)

    return

# Exec menu
def exec_menu(choice):
    os.system("cls" if sys.platform == "win32" else "clear")
    ch = choice.lower()
    if ch == "":
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection. Please try again.\n")
            menu_actions["main_menu"]()

# Helper function for obtaining credentials
def prompt_creds():
    username = None
    password = None
    flag = True

    os.system("cls" if sys.platform == "win32" else "clear")
    username = input("Enter your uniqname: ")
    while flag:
        password1 = getpass.getpass(prompt="Enter your umich password: ", stream=None)
        password2 = getpass.getpass(prompt="Re-enter to confirm password: ", stream=None)
        if password1 == password2:
            break
        print("Passwords do not match.")

    password = password1
    return (username, password)

# Helper function for obtaining date of signing in
def get_date():
    os.system("cls" if sys.platform == "win32" else "clear")
    m_valid = False

    while not m_valid:
        print("Please choose the month of your registration date: ")
        print("1. November")
        print("2. December")
        choice = input(">> ")

        try:
            month = months[choice]
            m_valid = True
        except KeyError:
            print("Invalid month selection.")

    d_valid = False
    while not d_valid:
        print("Please enter the day of your registration date (e.g. 1, 2, 3, or 30): ")
        choice = input(">> ")

        try:
            day = days[choice]
            d_valid = True
        except KeyError:
            print("Invalid day choice. Remember not to enter the 'rd', 'st' or 'th' of the date.")
            print("For example, enter '3' if you are registering on the third, not '3rd'.")

    h_valid = False
    while not h_valid:
        print("Please enter the hour of your registration date (in 24 hour military time).")
        choice = input(">> ")

        try:
            hour = int(choice)
            if hour >= 0 and hour <= 24:
                h_valid = True
            else:
                print("Invalid hour choice. Remember to enter an hour between 0 and 24.")
        except ValueError:
            print("Invalid hour choice. Remember to enter an integer and leave off AM or PM.")

    mi_valid = False
    while not mi_valid:
        print("Please enter the minute of your registration date.")
        choice = input(">> ")
        try:
            minute = int(choice)
            if minute >= 0 and minute <= 60:
                mi_valid = True
            else:
                print("Invalid minute choice. Remember to enter a minute between 0 and 60.")
        except ValueError:
            print("Invalid minute choice. It must be an integer between 0 and 60.")

    return EST.localize(datetime(2018, month, day, hour=hour, minute=minute))

def get_cookies():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(__file__)
        chromedriver_path = os.path.join(dir,"selenium","webdriver","chromedriver")
    else:
        chromedriver_path = "./chromedriver"

    nav_helper = NavHelper(chromedriver_path)
    username, password = prompt_creds()
    nav_helper.get_2Fcookies(username, password)

def run_now():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(__file__)
        chromedriver_path = os.path.join(dir,"selenium","webdriver","chromedriver")
    else:
        chromedriver_path = "./chromedriver"

    print("Starting AutoRegister ...")
    nav_helper = NavHelper(chromedriver_path)
    username, password = prompt_creds()
    print("***************************")
    print("Press CNTRL-C to quit running")
    print("***************************")
    nav_helper.login(username, password)
    nav_helper.nav()
    nav_helper.submit()

# Start running one minute early
def run_later():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(__file__)
        chromedriver_path = os.path.join(dir,"selenium","webdriver","chromedriver")
    else:
        chromedriver_path = "./chromedriver"

    print("Starting AutoRegister ...")
    nav_helper = NavHelper(chromedriver_path)
    reg_date = get_date()
    username, password = prompt_creds()
    print("***************************")
    print("Press CNTRL-C to quit running")
    print("***************************")

    print("Logging in!")
    nav_helper.login(username, password)
    nav_helper.nav()
    nav_helper.submit(reg_date=reg_date, now=False)

def quit():
    sys.exit()



# ==========================
#   DATETIME MENU SELECTIONS
# ==========================
months = {
    "1": 11,
    "2": 12,
    "3": 1,
}

days = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "25": 25,
    "26": 26,
    "27": 27,
    "28": 28,
    "29": 29,
    "30": 30,
}


# =======================
#    MENUS DEFINITIONS
# =======================


# Menu definitions
menu_actions = {
    "main_menu": main_menu,
    "1": run_now,
    "2": run_later,
    "3": get_cookies,
    "0": quit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    main_menu()
