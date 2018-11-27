from selenium import webdriver
from time import time
from datetime import datetime, timedelta


# If it doesn't go through, send the user a text/email
class NavHelper():

# This function creates a try except while loop to keep clicking
# on your selected id until it is successful. Lets the page wait for
# the page to loads.
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        from constants import LOGIN_URL
        self.driver.get(LOGIN_URL)
        self.driver.find_element_by_id("login").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("loginSubmit").click()
        return self.driver

    def get_2Fcookies(self):
        pass

    def load_2Fcookies(self):
        pass

    def clickit(self, id):
        stale_element = True
        before = time()
        while stale_element:
            try:
                self.driver.find_element_by_id(id).click()
                stale_element = False
            except:
                stale_element = True
                # Timeout
                after = time()
                if after - before > 80:
                    print("Timed out")
                    break

        return

    # This function selects all checkboxes on a webpage
    def sel_all(self):

        stale_element = True
        while stale_element:
            try:
                loaded = self.driver.find_element_by_xpath("//*[@type='checkbox']")
                boxes = self.driver.find_elements_by_xpath("//*[@type='checkbox']")
                stale_element = False
            except:
                stale_element = True

        for box in boxes:
            box.click()

        return

    # Navigate to backpack submit page
    def nav(self):
        from constants import STUD_WOL, STUD_SS, W19_ID, CONT_ID

        self.driver.get(STUD_WOL)
        self.driver.get(STUD_SS)
        self.driver.find_element_by_link_text("Backpack/ Registration").click()
        # Select winter 2019
        # Select in a loop to catch DOM changes after page load
        self.clickit(W19_ID)

        self.driver.find_element_by_id(CONT_ID).click()
        self.sel_all()

        return self.driver


    # keep clicking until it goes through?
    # This function sends the final submission
    def submit(self, **kwargs):
        from constants import P2_3, FIN_ID, EST
        unregistered = True

        try:
            now = kwargs["now"]
        except KeyError:
            now = True

        try:
            reg_date = kwargs["reg_date"]
        except KeyError:
            reg_date = None

        if now:
            self.clickit(P2_3)
            self.clickit(FIN_ID)
            return
        else:
            while unregistered:
                now = datetime.now(EST)
                diff = (now - reg_date).total_seconds()

                if diff >= 0:
                    print("Submitting ...")
                    self.clickit(P2_3)
                    self.clickit(FIN_ID)
                    unregistered = False
        return



### WAIT FOR DOM TO LOAD and do a try catch in a while loop
### INCREDIBLY USEFUL
