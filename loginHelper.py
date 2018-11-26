from selenium import webdriver
from constants import LOGIN_URL
from constants import driver


def login(username, password):
    driver.get(LOGIN_URL)
    driver.find_element_by_id("login").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("loginSubmit").click()
    return driver
