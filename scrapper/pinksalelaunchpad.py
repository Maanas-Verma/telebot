from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

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

time_period = 5
browser = create_driver(show_browser=False)

browser.get('https://www.pinksale.finance/launchpads/advanced?chain=BSC')  
time.sleep(time_period)
buttons =  browser.find_elements(by=By.CLASS_NAME, value='ant-pagination-item-link')
button = buttons[1]
while(button.get_attribute('disabled')==None):
    button.click()
    time.sleep(time_period)
    table_rows= browser.find_elements(By.XPATH,"/html/body/div[1]/section/section/main/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/table")
    x=[]
    for rows in table_rows:
        print(rows.text)
        x.append( rows.text)
    print(x)
    break

browser.quit()