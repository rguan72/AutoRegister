from selenium import webdriver
from constants import LOGIN_URL
from constants import driver


def login():
    driver.get(LOGIN_URL)
    driver.find_element_by_id("login").send_keys("guanr")
    driver.find_element_by_id("password").send_keys("c735qKBeAFbxi0G")
    driver.find_element_by_id("loginSubmit").click()
    return driver