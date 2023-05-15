import scrapy
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import parameter
import drivers
def login():
        global driver
        driver = webdriver.Chrome('/Users/username/bin/chromedriver')
        # driver.get method() will navigate to a page given by the URL address
        driver.get('https://www.linkedin.com')
        time.sleep(2)
        # locate email form by_class_name
        username = driver.find_element('id', 'session_key')
        # send_keys() to simulate key strokes
        username.send_keys(parameter.Linkedln_username)
        # sleep for 0.5 seconds
        time.sleep(0.5)
        # locate password form by_class_name
        password = driver.find_element('id', 'session_password')
        # send_keys() to simulate key strokes
        password.send_keys(parameter.Linkedln_password)
        time.sleep(0.5)
        # locate submit button by_xpath
        sign_in_button = driver.find_element('xpath', '//*[@type="submit"]')
        # .click() to mimic button click
        sign_in_button.click()
        time.sleep(2)
        print("Logged in Linkedln")