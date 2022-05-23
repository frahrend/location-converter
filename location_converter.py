# # Location Converter

# 
# In some Data Science projects it can be helpful to work with locations, as those can possibly give hints for patterns in weather predictions ....
# 
# Instead of inserting one location after the other into a location to coordinates converter and again insert those values into an array or dataframe, the goal of this project is to automate these worksteps which could otherwise take a long time for a large data set.
# 
# The steps that are to be solved to accomplish such automation are listed below.
# 
# Steps for this project is to produce a program that
# 
# 1.  takes location names from an array 
# 
# 2.  searches those at a website for the coordinates (float numbers, positive/negative numbers give indication about North, East, South and West of Null Island (longtitude, latitude = 0°N 0°E)
# 
# 5.  returns those two decimal numbers in a two-dimensional array that then can easily be added to a dataframe
# This program can then be used to replace locations to numeric values for e.g. generell Mapping or Machine Learning purposes.
# 
# 6. also, those steps are put together to copy and paste for your project; feel free to use it :)
# 


#import packages
import pandas as pd #software library for data manipulation and analysis
import selenium #to install selenium: conda install -c conda-forge selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Download Chromedriver on https://chromedriver.chromium.org/downloads

def locationConv (location):
    # Select the id box for location
    id_box = driver.find_element(By.CLASS_NAME, 'form-control')
    id_lat = driver.find_element(By.ID,'latitude')
    id_long = driver.find_element(By.ID,'longitude')
    #wait for page to have successfully loaded
    while (id_long.get_attribute('value') == ''):
        time.sleep(0.4)
    #remove longitude to later see if website has freshly returned coordinates 
    id_long.click()
    id_long.send_keys('\ue03d'+'a')
    id_long.send_keys(Keys.BACKSPACE)
    # Delete default entry 
    id_box.click()
    id_box.send_keys('\ue03d'+'a')
    id_box.send_keys(Keys.BACKSPACE)
    id_box.send_keys(location)
    # Click 'Get GPS Coordinates' button
    driver.find_element(By.XPATH, "//button[text()='Get GPS Coordinates']").click()
    #wait for page to have successfully loaded coordinates
    while (id_long.get_attribute('value') == ''):
        time.sleep(0.4)
    # Receive latitude and longitude of location
    latitude = float(id_lat.get_attribute('value'))
    longitude = float(id_long.get_attribute('value'))
    coordinates = [latitude, longitude]
    return coordinates


# Using Chrome to access web 
driver = webdriver.Chrome('/Users/franzi/GitHub/location-converter/chromedriver')
# Open the website 
driver.get('https://www.gps-coordinates.net/')
time.sleep(5)
coor = locationConv('Troy Alabama')
print(coor)

driver.quit()

