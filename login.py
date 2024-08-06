from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver_path = r"C:\Users\Abhinav\Desktop\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

web = webdriver.Chrome(service=service)


web.get("https://www.thesouledstore.com/login?redirect=%2Fmen")
    
   
login = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div/div/input"))
    )
login.send_keys("1234567890")

    
submit = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/form/button"))
    )
submit.click()


input("Press Enter to close the browser...")


web.quit()
