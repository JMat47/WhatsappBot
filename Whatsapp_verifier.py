from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
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

#names_list = ["Ragul VIT","Jerry Mathew"]

#names_list =["9884520487","8610913087","7338785720","7550093456","7358308477","9094033780","9840656355","8072998962","9790766239","9940549714","6383961592"]

donorData = pd.read_csv(r"C:\Users\jerry\OneDrive\Documents\Sender\Final.csv")
names_list = [list(row) for row in donorData.values]

for name in names_list:

    check = 0
    contact = driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
    print(name[2])
    contact.send_keys(name[2])
    contact.send_keys("\n")

    sleep(1)

    if(check_exists_by_xpath("//*[@id=\"pane-side\"]/div[1]/div/span")):
        #print("Not Found")
        check = 0
        closeButton = driver.find_element_by_class_name("_1Ek-U")
        closeButton.click()
        name.append("No")
        data = [name]
        column_names = ["Name", "BloodGroup", "PhoneNo","District","City","Whatsapp"]
        df = pd.DataFrame(data, columns=column_names)
        df.to_csv('Verification.csv',mode='a', index=False, header=False)
    else:
        #print("Found")
        check = 1
        name.append("Yes")
        data = [name]
        column_names = ["Name", "BloodGroup", "PhoneNo","District","City","Whatsapp"]
        df = pd.DataFrame(data, columns=column_names)
        df.to_csv('Verification.csv',mode='a', index=False, header=False)



sleep(5)
driver.quit()
