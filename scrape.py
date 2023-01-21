from scrapper.pinksalelaunchpad import scrape_pinksale
from db_manager.pandas_save import save_data_to_csv
from scrapper.thread_scrapping import parallet_extract_time_category
import time

while(True):
    print('new scrapping start')
    t = time.time()
    headings, tokens_data = scrape_pinksale()
    print('main page is scrapped')
    headings.append('Category')
    headings.append('start time')
    headings.append('end time')
    start_time, end_time, category = parallet_extract_time_category(tokens_data, 25)
    tokens_data['Category']=category
    tokens_data['start time']=start_time 
    tokens_data['end time']=end_time
    save_data_to_csv(headings, tokens_data, 'pinksale_launchpad.csv')
    print('total time taken: ', int(time.time()-t)//60, 'min', int(time.time()-t)%60, 'sec')
    print('------------------------------------------')
    time.sleep(1800-int(time.time()-t))