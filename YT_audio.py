#pip install selenium

#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class music():
    #constructor function -- initialize driver
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play_song(self, query):
        #self.query = query
        if query is None or not isinstance(query, str):
            print("Error: Query is not valid. Please provide a valid song name.")
            return

        self.driver.get(url="https://www.youtube.com/results?search_query=" + query) 
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')#first video title element
        video.click()
        time.sleep(90)

        self.driver.quit()


#assist = play_song()
#assist.play("risk by gracie abrams")
