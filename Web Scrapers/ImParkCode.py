from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time

#Must have chromedriver installed for Selenium to run
driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
names = []
address = [] #address of parking spots
price_per_hour = []

#initializes the url, but must be put in string format
def ImPark_Initial(url):
    driver.get(url)
    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="mapCanvas"]/div/div/div[13]/div/div[2]/div/button[2]')
    button.click()
    time.sleep(2)

content = driver.page_source
soup = BeautifulSoup(content)
lot_names = soup.findAll('div', attrs={'class':'lot-name'})
addresses = soup.findAll('span', attrs={'class':'address-text'})
prices = soup.findAll('div', attrs={'class':'lot-rate'})


def creating_csv(City, Province):
    for name in lot_names:
        if name not in names:
            names.append(name.text)

    for a in addresses:
        address.append(a.text + City + Province)

    for p in prices:
        price_per_hour.append(p.text)

    df = pd.DataFrame({'Lot Name': names, 'Address': address, 'Price': price_per_hour})
    df.to_csv(City + 'ImPark.csv', index=False, encoding='utf-8')
    driver.quit()

#CALL YOUR FUNCTIONS HERE!
