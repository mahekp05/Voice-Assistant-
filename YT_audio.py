from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By from Selenium
import time


class music():
    def __init__(self): #constructior funtion initatiting driver - chrome driver
        chrome_driver_path = r"C:\Users\mahek\chromedriver-win64\chromedriver.exe"         # Path to Chromedriver executable
        chrome_options = Options() #configure chrome options()
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options) #initialize chrome webdriver

    def play(self, query):
        self.query = query #query enetered
        #automatic search -- always same link except search topic added towards end
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query) #initiates driver
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')# Find the search first video title element
        video.click()         # Submit the search for video
        time.sleep(90)

#assist = music()
#assist.play("dynamite")