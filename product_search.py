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



web.get("https://www.thesouledstore.com/autocomplete")
    
    
time.sleep(1)
    
 
search = web.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/input")
search.send_keys("shirt")
search.send_keys(Keys.RETURN)
first = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/div[1]/div"))
    )

first.click()
   

input("Press Enter to close the browser...")


    
web.quit()
