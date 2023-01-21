from selenium.webdriver.common.by import By
import time

from scrapper.pinksalelaunchpad import create_driver
from scrapper.extractTokenProfile import extract_time_and_category
t = time.time()

from threading import Thread

class ScrapeTimeAndCategoryClass(Thread):
    
    def __init__(self, tokens_data):
        Thread.__init__(self)
        self.tokens_data = tokens_data
        self.start_time = None
        self.end_time = None
        self.category = None
        self.token_name = None
        
    def run(self):
        profile_links = self.tokens_data['profile_link']
        time_period = 10
        start_time_data = []
        end_time_data = []
        category_data = []
        token_name_data = []
        for index in range(len(profile_links)):
            error_last_time = False
            while(not error_last_time):
                try:
                    browser = create_driver(show_browser=False)
                    browser.get(profile_links[index])  
                    # print('link fetching -> wait for loading the page')
                    time.sleep(time_period)
                    title =  browser.find_elements(By.CLASS_NAME, "title")[0].text
                    # print(title, int(time.time()-t))

                    # for start time
                    tables = browser.find_elements(By.CLASS_NAME, "table-container")
                    table1 = tables[0].get_attribute('innerHTML')
                    table2 = tables[1].get_attribute('innerHTML')
                    browser.quit()
                    start_time, end_time, category = extract_time_and_category(title, table1, table2)
                    start_time_data.append(start_time)
                    end_time_data.append(end_time)
                    category_data.append(category)
                    token_name_data.append(self.tokens_data['Name'][index])
                    # print('done this link')
                    error_last_time = True
                except:
                    error_last_time = False
        self.start_time = start_time_data
        self.end_time = end_time_data
        self.category = category_data
        self.token_name = token_name_data

def parallet_extract_time_category(tokens_data, work_per_thread):
    selenium_threads = []
    numberOfTheads = len(tokens_data['Name'])//work_per_thread
    if(not (len(tokens_data['Name'])//work_per_thread)*work_per_thread==len(tokens_data['Name'])):
        numberOfTheads += 1
    # print(numberOfTheads, len(tokens_data))
    for i in range(numberOfTheads):
        end_index = (i+1)*work_per_thread
        if(i*work_per_thread+work_per_thread>len(tokens_data['Name'])):
            end_index = len(tokens_data['Name'])+1
        token_data_new = {}
        token_data_new['Name']=tokens_data['Name'][i*work_per_thread:end_index]
        token_data_new['profile_link'] = tokens_data['profile_link'][i*work_per_thread:end_index]
        selenium_threads.append(ScrapeTimeAndCategoryClass(token_data_new))
        selenium_threads[-1].start()
        # print(i*work_per_thread, end_index, 'starts')

    #checking for ending the threads
    for i in selenium_threads:
        i.join()

    # collect values
    start_time_arr = []
    end_time_arr = []
    category_arr = []
    for i in selenium_threads:
        start_time_arr += i.start_time
        end_time_arr += i.end_time
        category_arr += i.category
    print('time on threading',time.time()-t)
    return start_time_arr, end_time_arr, category_arr