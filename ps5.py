import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import winsound

options = Options()
options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430')
driver.maximize_window()
while True:
    try:
        #code with possible error
        driver.find_element_by_xpath('//*[@id="addToCartButton"]').click() #look for add to cart button
    except:
        driver.get('https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430') #if button not there, refresh page
    else:
        #the rest of the code
        time.sleep(1)
        driver.get('https://www.smythstoys.com/uk/en-gb/checkout/multi/payment-method/add') #go to fulfillment page after clicking add to cart
        break
winsound.Beep(800, 5000)
