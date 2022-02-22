'''
    This Module deals with all the Operations
    Related to the application
'''
def book_flight(browser):
    '''
        This function books a flight
        Selects Round Trip , One Way
        Select From and To
        Select Departure Date
        Passengers Seat = 1
        Select Search Flight Button

    '''
##Check if book a flight text is present
    book_a_flight = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[1]/h4")
    s = book_a_flight.text
    print("Element exist -" + s)

##Select Round Trip Option and then select One Way

    roundtrip = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[2]/div[2]/label/label")
    r = roundtrip.text
    print("Element selected -" + r)

    oneway = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[2]/div[1]/label/label")
    o = oneway.text
    print("Element selected -" + o)

##Enter FROM City as Delhi

    fromcity = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div[1]/div/div/input")
    fromcity.click()
    fcity =  fromcity.text
    print("Element selected -" + fcity)
    selectfromcity = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div[1]/div/div/div/div/div[2]")
    selectfromcity.click()
    city = selectfromcity.text
    print("From City selected ")

## Enter TO City as Budapest

    tocity = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div[2]/div/div/input")
    tocity.click()
    tcity = tocity.text

    #tocity.send_keys("Budapest")

    selecttocity = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div[2]/div/div/div/div/div[2]")
    selecttocity.click()
    print("To city selected")
##select Departure Date

    date = browser.find_element_by_xpath("/html/body/div[4]/section/div[2]/div[1]/div/div/div/div[3]/div[1]/form/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[4]/td[7]")
    date.click()
    print("Departure Date selected")

##Click On Search Flight

    searchbutton = browser.find_element_by_xpath(".//*[@id='bookFlightTab']/form/div[7]/div[9]/button/span[1]")
    searchbutton.click()
    print("Clicked on Search Button")