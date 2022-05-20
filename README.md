# Location-converter
Goal: Python Function to convert a name of a location to numeric, decimal coordinates  

To sucessfully run the code, you need to download Chromedriver from https://chromedriver.chromium.org/downloads. Download the version of the Chromedriver that equals your Chrome version. 
How to get the version of your Chrome: Three dots in the upper right corner of the chrome window --> Help --> About Google Chrome --> Version's digits before the first dot

When using the chromedriver for the first time, my Mac was showing me a warning about malware and did not want to open the chromedriver. 
On Mac this can be fixed in the System Preferences --> Security & Privacy --> Allow apps downloaded from: --> "'chromedriver' was blocked from use because it is not from an identified developer" --> Allow Anyway

Location can be manually changed by changing the string in following line of code: id_box.send_keys('Troy Alabama')

To receive coordinates, website 'https://www.gps-coordinates.net/' is used. 
