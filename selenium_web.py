#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By from Selenium
import time
import re  # regex operations -- used to manipulate text-based patterns

# Class to retrieve information from Wikipedia
class infow():
    def __init__(self):
        # Initialize the Chrome WebDriver without specifying path or options
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        if not query or not isinstance(query, str):
            print("Error: Query is not valid. Please provide a valid query.")
            return

        self.driver.get("https://www.wikipedia.org/")  # Navigate to Wikipedia homepage
        search_box = self.driver.find_element(By.XPATH, "//input[@id='searchInput']")  # Find the search input element using XPath
        search_box.send_keys(query)  # Enter the query text into the search box
        search_box.submit()  # Submit the search form

        # Wait for the page to load and retrieve the first paragraph of the search result
        time.sleep(2)
        try:
            first_paragraph = self.driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[1]")
            paragraph_text = first_paragraph.text  # Extract text from the paragraph
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph_text)
            if len(sentences) >= 2:
                first_two_sentences = ' '.join(sentences[:2])  # Get the first two sentences
            else:
                first_two_sentences = paragraph_text  # If less than two sentences, take the whole paragraph
            return first_two_sentences
        except Exception as e:
            print(f"Error retrieving information: {e}")
            return None

    def close_driver(self):
        self.driver.quit()  # Close the Chrome WebDriver instance
