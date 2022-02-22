'''
    This Module deals with all the Operations
    Related to the application
'''
def accept_cookie(browser):
    '''
        This function finds the temperature by
        scraping the page
    '''
   ## accept_cookies = browser.find_element_by_class_name("btn btn-primary btn-acc-cookie btn-acc-cookie-mob").click()

    accept_cookies = browser.find_element_by_xpath("/ html / body / div[5] / div[1] / div[19] / div / a / i").click()
    ##return int(temperature.text[:-2])
