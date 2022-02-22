import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

def select_flight(browser):
     time.sleep(60)
     oneway = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[6]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]")
     print(oneway.text)