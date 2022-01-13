from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path= './drivers/chromedriver')


list_of_addresses = []
price = []
duration = []


def init_data(url):
    driver.get(url)

def retrieve_data(City, Province):
    total_parking_spots = driver.find_elements(By.CLASS_NAME, 'LocationListItem__containerLink')
    print(len(total_parking_spots))
    for parking_spot in total_parking_spots:
            line_name = parking_spot.find_element(By.CLASS_NAME, 'LocationListItem__title')
            try:
                line_duration = parking_spot.find_element(By.CLASS_NAME,'LocationDetailsSearchDetails__detail__label')
            except:
                line_duration = None
            try:
                line_price = parking_spot.find_element(By.CLASS_NAME, 'LocationDetailsSearchDetails__detail__value')
            except:
                line_price = None
            list_of_addresses.append(line_name.text + " " + City + " , " + Province)
            if not line_duration == None and not line_price == None:
                duration.append(line_duration.text)
                price.append(line_price.text)
            else:
                duration.append("None")
                price.append("N/A")
    df = pd.DataFrame({'Lot Name': list_of_addresses, 'Price': price, 'Duration': duration})
    df.to_csv(City + 'Parkopedia.csv', index=False, encoding='utf-8')
    driver.quit()

init_data('https://en.parkopedia.ca/parking/locations/etobicoke_toronto_ontario_canada_47b0dpz2m3n47hs4bg/?arriving=202201091800&leaving=202201092000')
time.sleep(3)
retrieve_data("Etobicoke", "ON")

# #hello

