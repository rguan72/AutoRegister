import sys, os, time, subprocess, getpass
from datetime import datetime, timedelta
import pytz
from constants import EST
from selenium import webdriver
from loginHelper import login
from navHelper import nav, submit

# Main menu
def main_menu():
    while True:
        os.system("cls" if sys.platform == "win32" else "clear")
        print("Welcome to AutoRegister!")
        print("Please choose the menu you wish to start")
        print("1. Run Now")
        print("2. Run Later")
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
    print("Please choose the month of your registration date: ")
    print("1. November")
    print("2. December")
    choice = input(">> ")
    m_valid = False

    while  not m_valid:
        try:
            month = months[choice]
            m_valid = True
        except KeyError:
            print("Invalid month selection.")


    print("Please enter the day of your registration date (e.g. 1, 2, 3, or 30): ")
    choice = input(">> ")
    d_valid = False

    while not d_valid:
        try:
            day = days[choice]
            d_valid = True
        except KeyError:
            print("Invalid day choice. Remember not to enter the 'rd', 'st' or 'th' of the date.")
            print("For example, enter '3' if you are registering on the third, not '3rd'.")

    # Is this part necessary? Are they all at 9:15?
    # print("Please enter the hour of your registration date.")
    # choice = input(">> ")
    #
    return EST.localize(datetime(2018, month, day, hour=22, minute=19))



def run_now():
    print("Starting AutoRegister ...")
    username, password = prompt_creds()
    print("***************************")
    print("Press CNTRL-C to quit running")
    print("***************************")
    login(username, password)
    nav()
    submit()

# Start running one minute early
def run_later():
    print("Starting AutoRegister ...")
    reg_date = get_date()
    username, password = prompt_creds()
    print("***************************")
    print("Press CNTRL-C to quit running")
    print("***************************")
    now = datetime.now(EST)

    print(now)
    print(reg_date)
    diff = (now - reg_date).total_seconds()
    print(diff)

    if diff <= -60:
        print("Waiting ...")

    if diff >= -60:
        print("Logging in!")
        login(username, password)
        nav()

    if diff >= 0:
        print("Submitting ... ")
        submit()




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
    "0": quit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    main_menu()
