from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome()
driver.get("https://www.google.fr/flights/#flt=JOG.DPS.2018-09-28;c:IDR;e:1;px:2;sd:1;t:f;tt:o")
driver.implicitly_wait(5)
src = driver.page_source

f = open("result.txt", "w")
f.write(src)
