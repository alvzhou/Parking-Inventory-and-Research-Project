from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://parking.honkmobile.com/parking')
driver.implicitly_wait(5)
typing = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div/div[1]/input')
typing.send_keys('Edmonton, AB')
time.sleep(2)
typing.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div/div[2]/div[1]/div/div/span').click()
# button = driver.find_element(By.XPATH, '//*[@id="pageScrollWrapper"]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[13]/div/div[2]/div/button[2]')
# button.click()
# button.click()
# button.click()
time.sleep(5)


list_of_addresses = []
zone_address = []
price = []
duration = []

total_parking_spots = driver.find_elements(By.CLASS_NAME, 'MapZoneCard')

for parking_spot in total_parking_spots:
        line_name = parking_spot.find_element(By.CLASS_NAME, 'MapZoneCard--address')
        try:
            line_zone = parking_spot.find_element(By.CLASS_NAME, 'MapZoneCard--zoneId')
        except:
            line_zone = None
        try:
            line_price = parking_spot.find_element(By.CLASS_NAME, 'MapCardPriceComponent--price')
        except:
            line_price = None
        list_of_addresses.append(line_name.text + " ,Edmonton, AB")
        zone_address.append(line_zone.text)
        if not line_price == None:
            duration.append("2 Hours")
            price.append(line_price.text)
        else:
            duration.append("None")
            price.append("N/A")



df = pd.DataFrame({'Lot Name': list_of_addresses, 'Zone': zone_address, 'Price': price, 'Duration': duration})
df.to_csv('EdmontonHonkMobile.csv', index=False, encoding='utf-8')
driver.quit()

# #hello

