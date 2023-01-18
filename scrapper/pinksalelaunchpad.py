from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from scrapper.ps_scrapper import get_tokens_data, get_headings

def create_driver(show_browser: bool):
    """
    This function will return a browser driver with two options
    show the browser
    don't show the browser
    """
    if(show_browser):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

def append_data(data1, data2, headings):
    for i in range(len(headings)):
        data1[headings[i]]+= data2[headings[i]]
    return data1

def scrape_pinksale():
    time_period = 10
    browser = create_driver(show_browser=False)

    browser.get('https://www.pinksale.finance/launchpads/advanced?chain=BSC')  
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
    save_data_to_csv(headings, tokens_data)