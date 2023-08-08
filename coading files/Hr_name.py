import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Load data from a CSV file
df = pd.read_csv("A:/Masai Projects/Job Analytics project/Job_Data1.csv")

# Drop rows with missing values and save the cleaned data to a new CSV file
df.dropna(inplace=True)
df.to_csv("A:/Masai Projects/Job Analytics project/final_data.csv", index=False)

# Extract the 'Link' column values from the DataFrame
Link_L = []
for i in df['Link']:
    Link_L.append(i)

# Set up Selenium WebDriver using Chrome
service = Service('C:/Users/Mi/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(executable_path=r'C:/Users/Mi/Downloads/chromedriver_win32/chromedriver.exe')

HR_name = []

# Iterate through the list of links
try:
    for link in Link_L:
        driver.get(link)
        
        # Find the HR name element on the page and append to HR_name list
        try:
            hr_name = driver.find_element(By.CLASS_NAME, "rec-name").text
            HR_name.append(hr_name)
        except:
            HR_name.append("NA")
        print(len(HR_name))
except:
    print("NA")

# Create a new DataFrame with HR names
df_hr = pd.DataFrame({"HR_Name": HR_name})

# Save the new DataFrame to a CSV file
df_hr.to_csv("A:/Masai Projects/Job Analytics project/hr_exp.csv", index=False)
print(df_hr)
