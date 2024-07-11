#pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By from Selenium
import time
import re #regex operations -- used to manipulated text based patterns


#download chrome dirver + add to system var : https://googlechromelabs.github.io/chrome-for-testing/#stable OR https://sites.google.com/chromium.org/driver/downloads
#command prompt -- where chromedriver
class infow():
    def __init__(self):
        chrome_driver_path = r"C:\Users\mahek\chromedriver-win64\chromedriver.exe"         # Path to Chromedriver executable
        chrome_options = Options() #configure chrome options()
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options) #initialize chrome webdriver

    def get_info(self, query):
        self.query = query 
        self.driver.get("https://www.wikipedia.org/") #navigate to wikipedia home page
        search_box = self.driver.find_element(By.XPATH, "//input[@id='searchInput']")          # Find the search input element using XPath
        search_box.send_keys(self.query)        # Enter the query text into the search box
        search_box.submit()         # Submit the search form
        
        first_paragraph = self.driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[1]")
        paragraph_text = first_paragraph.text # Extract text from the paragraph
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph_text)
        if len(sentences) >= 2:
            first_two_sentences = ' '.join(sentences[:1])
        else:
            first_two_sentences = paragraph_text  # If less than two sentences, take the whole paragraph
        #print(first_two_sentences)
        return first_two_sentences

        time.sleep(30)

    def close_driver(self):
        self.driver.quit()         # Close the Chrome webdriver instance

# Instantiate infow class
 # Call the get_info method to perform a search

time.sleep(30)  # Keeps the browser open for 5 seconds before closing


