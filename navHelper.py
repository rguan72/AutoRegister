from selenium import webdriver
from time import time
from bs4 import BeautifulSoup
from loginHelper import login
from constants import driver
from constants import BACK_REG_ID, STUD_WOL, STUD_SS, W19_ID, CONT_ID, P2_3, FIN_ID
# TODO: rename constants to make more readable


# If it doesn't go through, send the user a text/email

def stale_click(func):
    def f(*args, **kwargs):
        stale_element = True
        while stale_element:
            try:
                rv = f(*args, **kwargs)
                stale_element = False
            except:
                stale_element = True
        return rv
    return f

def clickit(driver, id):
    # This function creates a try except while loop to keep clicking
    # on your selected id until it is successful. Lets the page wait for
    # the page to loads.
    stale_element = True
    before = time()
    while stale_element:
        try:
            driver.find_element_by_id(id).click()
            stale_element = False
        except:
            stale_element = True
            # Timeout
            after = time()
            if after - before > 20:
                print "Timed out"
                break

    return

def sel_all(driver):

    stale_element = True
    while stale_element:
        try:
            loaded = driver.find_element_by_xpath("//*[@type='checkbox']")
            boxes = driver.find_elements_by_xpath("//*[@type='checkbox']")
            stale_element = False
        except:
            stale_element = True

    for box in boxes:
        box.click()

    return

def nav():
    # Navigate to backpack page
    driver.get(STUD_WOL)
    driver.get(STUD_SS)
    driver.find_element_by_link_text("Backpack/ Registration").click()
    # Select winter 2019
    # Select in a loop to catch DOM changes after page load
    clickit(driver, W19_ID)

    driver.find_element_by_id(CONT_ID).click()
    sel_all(driver)
    clickit(driver, P2_3)
    clickit(driver, FIN_ID)

    return driver


### WAIT FOR DOM TO LOAD and do a try catch in a while loop
### INCREDIBLY USEFUL
