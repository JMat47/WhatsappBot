from bs4.builder import HTML_5
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


from selenium.common.exceptions import NoSuchElementException        
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome(executable_path=r"C:\Users\jerry\OneDrive\Documents\Sender\chromedriver.exe")

driver.get("https://web.whatsapp.com/")

waitForVerification = input()
sleep(2)

#names_list = ["Ragul VIT","Jerry Mathew","8975656","Amma","varun Nair","8976895654"]
names_list =["9884520487","8610913087","7338785720","7550093456","7358308477","9094033780","9840656355","8072998962","9790766239","9940549714","6383961592"]

for name in names_list:

    check = 0
    contact = driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
    contact.send_keys(name)
    contact.send_keys("\n")

    sleep(1)

    if(check_exists_by_xpath("//*[@id=\"pane-side\"]/div[1]/div/span")):
        #print("Not Found")
        check = 0
        sleep(1)
        closeButton = driver.find_element_by_class_name("_1QWS8")
        closeButton.click()
    else:
        #print("Found")
        check = 1

    if(check == 1):
        message = driver.find_element_by_class_name("_11liR")
        extracted = message.text.lower().replace("yesterday","").replace("yes/no","")
        print( name , "yes" in extracted)
        print(extracted)


sleep(5)

driver.quit()