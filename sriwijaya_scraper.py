from selenium import  webdriver
import time

startTime = time.time()

vvFlight = False
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome()
driver.get('https://sriwijayaair.co.id/')
driver.implicitly_wait(3)

fromSrc=driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
        "//div[@class='col-md-4'][2]"+
        "//span[@class='filter-option pull-left']")
driver.execute_script("arguments[0].innerText='CGK'", fromSrc)

toSrc=driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
        "//div[@class='col-md-4'][3]"+
        "//span[@class='filter-option pull-left']")
driver.execute_script("arguments[0].innerText='JOG'", toSrc)

if vvFlight:
    flightType = driver.find_element_by_xpath("//form[@id='searchFlightForm']" +
            "//div[@class='col-md-4'][1]"+
            "//span[@class='bootstrap-switch-label']")
    flightType.click()

departDate = driver.find_element_by_xpath("//input[@id='departureDate']")
departDate.send_keys("15-Sep-2018")

print(time.time() - startTime)
