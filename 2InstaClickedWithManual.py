from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate
import time

# Google Sheets CSV URL
sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df)
print(tabulate(df, headers='keys', tablefmt='psql'))

# Updated path to the ChromeDriver executable
chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# Updated path to the custom Chrome executable
chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# Set Chrome options to point to the custom Chrome executable
chrome_options = Options()
chrome_options.binary_location = chrome_exe_path

# Create a Service object for ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Manually set the row index to test
row_index = 2  # Change this index manually to test different rows

try:
    # Initialize the WebDriver with the Service object and Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open Google
    driver.get('https://google.com')
    
    # Process the specific row based on row_index
    if row_index < len(df):
        row = df.iloc[row_index]
        name = row['NAME']
        location_zip = row['LOCATION_ZIP']
        location_street = row['LOCATION_STREET']
        
        # Construct search query
        search_query = f"{name} {location_street} {location_zip}"
        
        # Print search query
        print(f"\nProcessing Entry {row_index + 1}/{len(df)}")
        print(f"Search Query: {search_query}")
        
        # Locate the search box and perform the search
        search_box = driver.find_element("name", "q")
        search_box.clear()  # Clear the previous query
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Print the current URL after search
        search_url = driver.current_url
        print(f"Search URL: {search_url}")
        
        # Wait for results to load
        time.sleep(5)
        
        # Print search results page title
        print(driver.title)
        
        # Find Instagram links in the search results
        search_results = driver.find_elements("css selector", "a")
        found = False
        for result in search_results:
            href = result.get_attribute("href")
            if href and "instagram.com" in href:
                print(f"Found Instagram link: {href}")
                result.click()
                found = True
                break  # Click the first Instagram link found
        
        if not found:
            print("No Instagram link found.")
        
    else:
        print("Row index out of range.")
    
    # Wait indefinitely to keep the browser open
    input("Press Enter to keep the browser open and exit...")

finally:
    # No action needed in the finally block if not closing the browser
    pass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate
import time

# Google Sheets CSV URL
sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df)
print(tabulate(df, headers='keys', tablefmt='psql'))

# Updated path to the ChromeDriver executable
chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# Updated path to the custom Chrome executable
chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# Set Chrome options to point to the custom Chrome executable
chrome_options = Options()
chrome_options.binary_location = chrome_exe_path

# Create a Service object for ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Manually set the row index to test
row_index = 2  # Change this index manually to test different rows

try:
    # Initialize the WebDriver with the Service object and Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open Google
    driver.get('https://google.com')
    
    # Process the specific row based on row_index
    if row_index < len(df):
        row = df.iloc[row_index]
        name = row['NAME']
        location_zip = row['LOCATION_ZIP']
        location_street = row['LOCATION_STREET']
        
        # Construct search query
        search_query = f"{name} {location_street} {location_zip}"
        
        # Print search query
        print(f"\nProcessing Entry {row_index + 1}/{len(df)}")
        print(f"Search Query: {search_query}")
        
        # Locate the search box and perform the search
        search_box = driver.find_element("name", "q")
        search_box.clear()  # Clear the previous query
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Print the current URL after search
        search_url = driver.current_url
        print(f"Search URL: {search_url}")
        
        # Wait for results to load
        time.sleep(5)
        
        # Print search results page title
        print(driver.title)
        
        # Find Instagram links in the search results
        search_results = driver.find_elements("css selector", "a")
        found = False
        for result in search_results:
            href = result.get_attribute("href")
            if href and "instagram.com" in href:
                print(f"Found Instagram link: {href}")
                result.click()
                found = True
                break  # Click the first Instagram link found
        
        if not found:
            print("No Instagram link found.")
        
    else:
        print("Row index out of range.")
    
    # Wait indefinitely to keep the browser open
    input("Press Enter to keep the browser open and exit...")

finally:
    # No action needed in the finally block if not closing the browser
    pass
