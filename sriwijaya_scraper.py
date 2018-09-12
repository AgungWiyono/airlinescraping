from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Flight Description
vvFlight = False
depart = "'Sat Sep 15 2018 20:59:07 GMT+0700'"
returnd = "'Thu Sep 20 2018 00:00:00 GMT+0700'"
pas = ['2', '1', '1']

startTime = time.time()

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome()
#driver = webdriver.Chrome(chrome_options=options)
driver.get('https://sriwijayaair.co.id/')
driver.implicitly_wait(3)

# If the flight type is return
if vvFlight:

    # Click return button
    flightType = driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
            "//div[@class='col-md-4'][1]"+
            "//span[@class='bootstrap-switch-label']")
    flightType.click()

    #Set return date
    driver.implicitly_wait(3)
    retDate=driver.find_element_by_xpath("//span[@id='returnDate_stamp']")
    driver.execute_script("arguments[0].setAttribute('style','display:block')",
                          retDate)
    driver.execute_script("arguments[0].innerText="+returnd,retDate)


# Set Departure AirPort
fromSrc=driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
        "//div[@class='col-md-4'][2]"+
        "//span[@class='filter-option pull-left']")
fromSrc.click()
fromSrcfield = driver.find_element_by_xpath("//div[@class='btn-group "+
"bootstrap-select form-control show-tick tx-blue tx-bold select-picker "+
"open']//input[@class='form-control']")
fromSrcfield.send_keys("CGK")
fromSrcfield.send_keys(Keys.RETURN)

'''
# Set Arrival AirPort
toSrc=driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
        "//div[@class='col-md-4'][3]"+
        "//span[@class='filter-option pull-left']")
driver.execute_script("arguments[0].innerText='JOG'", toSrc)

# Set Departure Date
departDate = driver.find_element_by_xpath("//span[@id='departureDate_stamp']")
driver.execute_script("arguments[0].setAttribute('style','display:block')",
                      departDate)
driver.execute_script("arguments[0].innerText="+depart,departDate)

# Set adult passenger value
adult = driver.find_element_by_xpath("//input[@id='AdultSrc']")
driver.execute_script("arguments[0].setAttribute('value','"+pas[0]+"')",
                      adult)

# Set child passenger value
child = driver.find_element_by_xpath("//input[@id='ChildSrc']")
driver.execute_script("arguments[0].setAttribute('value','"+pas[1]+"')",
                      child)

# Set infant passenger value
infant = driver.find_element_by_xpath("//input[@id='InfantSrc']")
driver.execute_script("arguments[0].setAttribute('value','"+pas[2]+"')",
                      infant)

# Submit Form
submit = driver.find_element_by_xpath("//a[@id='redeemMiles']")
submit.click()
'''
