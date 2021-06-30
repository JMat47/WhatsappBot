## Initializing Depedancies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException  

## Function to check wether a particular element exists
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

## Loading Chrome Driver
driver = webdriver.Chrome(executable_path=r"C:\Users\jerry\OneDrive\Documents\Sender\chromedriver.exe")

## Loading Whatsapp Web
driver.get("https://web.whatsapp.com/")

## Check function (Enter any key after Scanning QR code):
waitForVerification = input()
sleep(2)

## List of Numbers to send the message to
names_list = ["6383961592"]

#names_list =["9884520487","8610913087","7338785720","7550093456","7358308477","9094033780","9840656355","8072998962","9790766239","9940549714","6383961592"]

## Loop to send Messages to people in names_list
for name in names_list:

    ## Searching for Contact
    contact = driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
    contact.send_keys(name)
    contact.send_keys("\n")

    ## Wait for contact to load
    sleep(1)

    ## Sending the Message
    message = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[2]/div/div[2]")
    message.send_keys("Hello,")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("I’m really sorry for interrupting your day, but we're a group of student volunteers that have set an initiative to make receiving blood easier.  Over the past few months we’ve seen many people struggle to get details of verified blood donors. We wanted to help in the smallest way we could and we would love your help in doing so.")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("If you could confirm the following details below you could be saving a life.")
    message.send_keys("\n")
    

## Quit the chrome driver
sleep(5)
driver.quit()



