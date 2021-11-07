from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import numpy as np

import datetime as dt
import warnings
warnings.filterwarnings('ignore')
import win32com.client as win32

class WebScraper:
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        url = 'https://www.cnbc.com/bonds/'
        self.driver.get(url)
        time.sleep(5)

        try:
            self.driver.find_elements_by_tag_name('button')[-2].click()
            time.sleep(5)
        except:
            pass

    def cds_scrape(self):

        self.driver.get('https://www.cnbc.com/'+'sovereign-credit-default-swaps/')

        names=([name.text for name in BeautifulSoup(self.driver.page_source,'html').findAll("td", {"data-field":"symbol"}) ])
        px=([name.text for name in BeautifulSoup(self.driver.page_source,'html').findAll("td", {"data-field":"last"}) ])
        change=([name.text for name in BeautifulSoup(self.driver.page_source,'html').findAll("td", {"data-field":"change"}) ])
        change_pct=([name.text for name in BeautifulSoup(self.driver.page_source,'html').findAll("td", {"data-field":"change_pct"}) ])

        data=pd.DataFrame({'Name':names,'Price':px,'Change':change,'Change_pct':change_pct})
        data.insert(0,'Date',dt.datetime.now().strftime('%Y-%m-%d'))

        self.driver.close()
        self.driver.quit()

        return data
