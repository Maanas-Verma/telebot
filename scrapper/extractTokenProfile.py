from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from pinksalelaunchpad import create_driver

def extractCategory(tokens_data):
    profile_links = tokens_data['profile_link']
    time_period = 10
    for link in profile_links:
        browser = create_driver(show_browser=False)
        browser.get(link)  
        time.sleep(time_period)
        button =  browser.find_elements(by=By.CLASS_NAME, value='ant-pagination-item-link')[1]
        table_rows= browser.find_elements(By.XPATH,"/html/body/div[1]/section/section/main/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/table")
        headings = get_headings(table_rows[0].get_attribute('innerHTML'))
        tokens_data = {}
        for head in headings: tokens_data[head]=[]
        tokens_data = append_data(tokens_data, get_tokens_data(table_rows[0].get_attribute('innerHTML')), headings)
        while(button.get_attribute('disabled')==None):
            button.click()
            time.sleep(time_period)
            table_rows= browser.find_elements(By.XPATH,"/html/body/div[1]/section/section/main/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/table")
            tokens_data = append_data(tokens_data, get_tokens_data(table_rows[0].get_attribute('innerHTML')), headings)

        browser.quit()
        return headings, tokens_data