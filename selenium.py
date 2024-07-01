from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome('C:\Sandbox\chromedriver.exe')  # Replace with your path to chromedriver

# Open a webpage
driver.get("https://www.example.com")

# Interact with elements (e.g., search bar)
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium with Python")
search_box.send_keys(Keys.RETURN)

# Wait for the page to load (optional)
time.sleep(2)

# Extract information (e.g., search results)
results = driver.find_elements_by_xpath("//h3[@class='r']/a")
for result in results[:5]:
    print(result.text)
    print(result.get_attribute("href"))

# Close the WebDriver
driver.quit()
