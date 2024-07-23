from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Use the correct path to the chromedriver executable
driver_path = r"C:\Users\Abhinav\Desktop\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Initialize WebDriver
web = webdriver.Chrome(service=service)


    # Navigate to the website
web.get("https://www.thesouledstore.com/autocomplete")
    
    # Allow some time for the page to load
time.sleep(1)
    
    # Find the login input field and enter the phone number
search = web.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/input")
search.send_keys("shirt")
search.send_keys(Keys.RETURN)

   

    # Wait for user input to close the browser
input("Press Enter to close the browser...")


    # Close the WebDriver session
web.quit()