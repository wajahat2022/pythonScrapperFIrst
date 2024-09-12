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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

try:
    # Initialize the WebDriver with the Service object and Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open Google
    driver.get('https://google.com')
    
    # Get the first row of data
    first_row = df.iloc[0]
    name = first_row['NAME']
    location_zip = first_row['LOCATION_ZIP']
    location_street = first_row['LOCATION_STREET']
    
    # Construct search query for restaurant data
    search_query = f"{name} {location_street} {location_zip}"
    
    # Print search query
    print(f"Search Query: {search_query}")
    
    # Locate the search box and perform the search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    time.sleep(5)
    
    # Print the current URL after search
    search_url = driver.current_url
    print(f"Search URL: {search_url}")
    
    # Check for Instagram profile URL in the search results
    try:
        # Look for Instagram profile link in search results
        profile_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'instagram.com')]")
        
        if profile_links:
            profile_url = profile_links[0].get_attribute("href")
            print(f"Instagram Profile Found: {profile_url}")
            
            # Click on the Instagram profile link
            profile_links[0].click()
            print(f"Visiting Instagram Profile: {profile_url}")
        else:
            print("Instagram profile not found.")
    
    except Exception as e:
        print(f"Error while searching for Instagram profile: {e}")
    
    # Wait indefinitely to keep the browser open
    input("Press Enter to keep the browser open and continue...")

finally:
    # No action needed in the finally block if not closing the browser
    pass
