## Initializing Depedancies

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException  
import pandas as pd

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
#names_list = ["9176684086" , "Jerry","73585 79588","98845 20487"]

donorData = pd.read_csv(r"C:\Users\jerry\OneDrive\Documents\Sender\Final_Data.csv")
names_list = [list(row) for row in donorData.values]
print(names_list)

## Loop to send Messages to people in names_list
for name in names_list:

    ## Searching for Contact
    contact = driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
    contact.send_keys(name[2])
    contact.send_keys("\n")

    ## Wait for contact to load
    sleep(0.5)

    ## Sending the Message
    message = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[2]/div/div[2]")
    message.send_keys("Trial 4 : Hello,")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("Apologies for interrupting your day. We are a group of students who have put forward an initiative to make receiving and donating blood an easier process. Over the last year we have seen many people struggle to get verified donors. We wanted to help them in the smallest way we could, and we would love your help in doing so.")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("If you could confirm the following details below you could be saving a life.")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("-> *Your Blood Group is: {}*".format(name[1]))
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("-> *Your are currently in: {}*".format(name[4]))
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("-> *You are still a donor*" )
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("If the above mentioned details are correct reply with a *YES* or else a *NO*" )
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("We hope we can make an impact soon and for you to be a part of it would mean alot to us. Have a wonderful day. " )
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys(Keys.SHIFT, "\n")
    message.send_keys("P.S: this is an automated message, if you have any queries or doubts feel free to email us at blodindia@gmail.com" )
    message.send_keys("\n")

    # Logging Data for verification
    name.append("Sent")
    data = [name]
    column_names = ["Name", "BloodGroup", "PhoneNo","District","City","Whatsapp"]
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv('Send_log.csv',mode='a', index=False, header=False)
    

## Quit the chrome driver
sleep(5)
driver.quit()
