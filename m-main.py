from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from selenium.webdriver.common.by import By


df= pd.read_excel(r"Number.xlsx")





options = Options()
options.add_argument("C:\\Users\\DCL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 7")
options.add_argument("user-data-dir=c:\\tmp\\newdir")
options.add_argument("profile-directory=Profile 7")
driver = webdriver.Chrome(options=options)
for index , row in df.iterrows():
    mobile_number= "+880"+ str(row["Number"])
    driver.get("https://t.me/"+mobile_number)
    time.sleep(5)
    onpen_in_web=driver.find_element(By.XPATH, "//span[@class='tgme_action_button_label']")
    onpen_in_web.click()
    time.sleep(1)
    text_box = driver.find_element(By.XPATH, "//div[@id='editable-message-text']")
    text_box.click()
    time.sleep(1)
    text_box.send_keys("hello")
    time.sleep(1)
    send_button= driver.find_element(By.XPATH, "(//button[@title='Send Message'])[1]")
    send_button.click()
    time.sleep(1)

