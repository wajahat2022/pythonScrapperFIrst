# i am doing manuually data entry jjob where i i have a sheet with 3 column which need to be copied like below 

# Silva's Sports Bar	3672 S Bristol St	92704

# which is named column for 
# NAME	LOCATION_ZIP	LOCATION_STREET respectively 


# i need to manually copy each entry and paste it to chrome to get respective restaurant and i have too look in first page about instagram of that restaurant if have any like in this case 
# https://www.instagram.com/SilvasSportsBar/



# i go to thhat page manually and THEN I AM SCRAPPING PROFILE PIC OF THAT AND THERE IS 3RD COLUMN WHICH HAS id so the profile pictuure i am saving should be saved with that id in 4 column then we have to go to next entry and have to search instagram profile pic if have any and if instagram is fouund and profile picture is saved with that id value present in 4 

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
# import pandas as pd 
# from tabulate import tabulate

# sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
# df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# print(df)
# print(tabulate(df, headers='keys', tablefmt='psql'))
# # Updated path to the ChromeDriver executable
# chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# # Updated path to the custom Chrome executable
# chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# # Set Chrome options to point to the custom Chrome executable
# chrome_options = Options()
# chrome_options.binary_location = chrome_exe_path

# # Create a Service object for ChromeDriver
# service = Service(executable_path=chrome_driver_path)

# try:
#     # Initialize the WebDriver with the Service object and Chrome options
#     driver = webdriver.Chrome(service=service, options=chrome_options)
    
#     # Open a website
#     driver.get('https://google.com')
    
#     # Wait indefinitely to keep the browser open
#     input("Press Enter to close the browser...")

# finally:
#     # No action needed in the finally block if not closing the browser
#     pass

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
# from tabulate import tabulate
# import time

# # Google Sheets CSV URL
# sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
# df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# print(df)
# print(tabulate(df, headers='keys', tablefmt='psql'))

# # Updated path to the ChromeDriver executable
# chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# # Updated path to the custom Chrome executable
# chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# # Set Chrome options to point to the custom Chrome executable
# chrome_options = Options()
# chrome_options.binary_location = chrome_exe_path

# # Create a Service object for ChromeDriver
# service = Service(executable_path=chrome_driver_path)

# try:
#     # Initialize the WebDriver with the Service object and Chrome options
#     driver = webdriver.Chrome(service=service, options=chrome_options)
    
#     # Open Google
#     driver.get('https://google.com')
    
#     # Get the first row of data
#     first_row = df.iloc[0]
#     name = first_row['NAME']
#     location_zip = first_row['LOCATION_ZIP']
#     location_street = first_row['LOCATION_STREET']
    
#     # Construct search query
#     search_query = f"{name} {location_street} {location_zip}"
    
#     # Print search query
#     print(f"Search Query: {search_query}")
    
#     # Locate the search box and perform the search
#     search_box = driver.find_element("name", "q")
#     search_box.send_keys(search_query)
#     search_box.send_keys(Keys.RETURN)
    
#     # Print the current URL after search
#     search_url = driver.current_url
#     print(f"Search URL: {search_url}")
    
#     # Wait for results to load
#     time.sleep(5)
    
#     # Print search results page title
#     print(driver.title)
    
#     # Wait indefinitely to keep the browser open
#     input("Press Enter to keep the browser open and continue...")

# finally:
#     # No action needed in the finally block if not closing the browser
#     pass
# waj second 
# i am doing manuually data entry jjob where i i have a sheet with 3 column which need to be copied like below 

# Silva's Sports Bar	3672 S Bristol St	92704

# which is named column for 
# NAME	LOCATION_ZIP	LOCATION_STREET respectively 


# i need to manually copy each entry and paste it to chrome to get respective restaurant and i have too look in first page about instagram of that restaurant if have any like in this case 
# https://www.instagram.com/SilvasSportsBar/



# i go to thhat page manually and THEN I AM SCRAPPING PROFILE PIC OF THAT AND THERE IS 3RD COLUMN WHICH HAS id so the profile pictuure i am saving should be saved with that id in 4 column then we have to go to next entry and have to search instagram profile pic if have any and if instagram is fouund and profile picture is saved with that id value present in 4 

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
# import pandas as pd 
# from tabulate import tabulate

# sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
# df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# print(df)
# print(tabulate(df, headers='keys', tablefmt='psql'))
# # Updated path to the ChromeDriver executable
# chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# # Updated path to the custom Chrome executable
# chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# # Set Chrome options to point to the custom Chrome executable
# chrome_options = Options()
# chrome_options.binary_location = chrome_exe_path

# # Create a Service object for ChromeDriver
# service = Service(executable_path=chrome_driver_path)

# try:
#     # Initialize the WebDriver with the Service object and Chrome options
#     driver = webdriver.Chrome(service=service, options=chrome_options)
    
#     # Open a website
#     driver.get('https://google.com')
    
#     # Wait indefinitely to keep the browser open
#     input("Press Enter to close the browser...")

# finally:
#     # No action needed in the finally block if not closing the browser
#     pass


# ----- 
# third 

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Google Sheets CSV URL
sheet_id = '1MQGvVQMZcRreOW_3d8UaCmmEni6ttE618cII2yTsJz0'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# Updated path to the ChromeDriver executable
chrome_driver_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome web driver\chromedriver-win64\chromedriver.exe"

# Updated path to the custom Chrome executable
chrome_exe_path = r"C:\Users\RGB PC GAMER\Desktop\pythhon scrapper\Chrome\chrome-win64\chrome.exe"

# Set Chrome options to point to the custom Chrome executable
chrome_options = Options()
chrome_options.binary_location = chrome_exe_path
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Create a Service object for ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Function to process a single row manually
def process_row(row_index):
    # Initialize the WebDriver with the Service object and Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Google
        driver.get('https://google.com')
        
        # Get the data from the current row
        row = df.iloc[row_index]
        name = row['NAME']
        location_zip = row['LOCATION_ZIP']
        location_street = row['LOCATION_STREET']
        
        # Construct search query for restaurant data
        search_query = f"{name} {location_street} {location_zip}"
        
        # Print search query for checking
        print(f"Search Query ({row_index+1}): {search_query}")
        
        # Locate the search box and perform the search
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()  # Clear the search box before entering new search
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(3)
        
        # Print the current URL after search
        search_url = driver.current_url
        print(f"Search URL: {search_url}")
        
        # Scroll down slightly to ensure visibility
        driver.execute_script("window.scrollBy(0, 200);")
        
        # Wait for the Instagram profile link to be clickable
        try:
            profile_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'instagram.com')]"))
            )
            profile_url = profile_link.get_attribute("href")
            print(f"Instagram Profile Found for {name}: {profile_url}")
            
            # Scroll to the Instagram profile link to ensure visibility
            driver.execute_script("arguments[0].scrollIntoView(true);", profile_link)
            time.sleep(1)  # Pause briefly after scrolling

            # Retry clicking if intercepted
            attempts = 0
            while attempts < 3:
                try:
                    profile_link.click()
                    print(f"Visiting Instagram Profile: {profile_url}")
                    break
                except Exception as e:
                    print(f"Click failed, retrying... ({attempts+1}/3)")
                    time.sleep(2)
                    attempts += 1
            
        except Exception as e:
            print(f"Instagram profile not found or error for {name}: {e}")
        
        # Keep the browser open until user proceeds
        input("Press Enter to process the next entry...")

    finally:
        driver.quit()  # Close the browser after each entry
    
    # Return the updated row index
    return row_index

# Manual control for selecting the row index
row_index = int(input("Enter the row index to start with (0-based index): "))

# Process the current row based on the provided row_index
process_row(row_index)

# Add a loop for manual control to proceed or exit
while row_index < len(df):
    user_input = input("Type 'next' to process the next entry or 'exit' to stop: ").strip().lower()
    
    if user_input == 'next':
        row_index += 1  # Move to the next row
        process_row(row_index)
    elif user_input == 'exit':
        print("Exiting the script.")
        break
    else:
        print("Invalid input. Please type 'next' or 'exit'.")
