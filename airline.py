'''
    This is the main file of the project, This is a simple
    demostration of the complete automated shopping system.
    Pylint Testing Rate for this file = 10/10.
'''
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from libs.accept_cookie import accept_cookie
from libs.book_flight import book_flight
from selenium.webdriver.chrome.options import Options

#Driver code
from libs.select_flight import select_flight

if __name__ == "__main__":
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.goindigo.in/")
    browser.maximize_window()
    if browser.title == "Book Domestic & International Flights at Lowest Airfare - IndiGo":
        print("IndiGo Airline Website is Launched")
    else:
        print("Error - Wrong website")

    accept_cookie(browser)
    print("Please select your flight")
    book = book_flight(browser)
    print("Flight Search Completed")
    browser.close()
