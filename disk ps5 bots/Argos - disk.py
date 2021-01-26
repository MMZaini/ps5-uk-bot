import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import winsound

print("This program comes with ABSOLUTELY NO WARRANTY; for details check included license. This is free software, and you are welcome to redistribute it under certain conditions; check license for conditions.")

item = 'https://www.argos.co.uk/product/8349000' # Variable for the item wanted
options = Options()
options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(item)
while True:
    try:
        # Code with possible error - error being that there's no add to cart button
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[3]/div[1]/section[2]/section/div[15]/div/div[2]/button').click() # Looks for the 'add to cart button' using xpath
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[3]/div[1]/section[2]/section/div[10]/div[3]/div[2]/div[5]/button').click() # Tries to atc as delivery
    except:
        driver.get(item)# If the atc button cannot be found, refresh until it is found
    else:
        time.sleep(1)
    driver.get('https://www.argos.co.uk/basket') # Goes to basket
    driver.find_element_by_xpath('//*[@id="basket-content"]/main/div[2]/section[3]/div[2]/div[2]/div/div/form/button').click() # Goes to checkout
    break

winsound.Beep(899, 5000) # Makes a beep sound for 5 seconds/5k ms to notify the user that the item is in stock and at checkout page



