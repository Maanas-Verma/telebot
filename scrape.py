from scrapper.pinksalelaunchpad import scrape_pinksale
from db_manager.pandas_save import save_data_to_csv
from scrapper.thread_scrapping import parallet_extract_time_category
import time
from threading import Thread

class ScrapeThread (Thread):
   def __init__(self):
      Thread.__init__(self)
   def run(self):
        while(True):
            print('new scrapping start')
            t = time.time()
            headings, tokens_data = scrape_pinksale()
            print('main page is scrapped')
            headings.append('Category')
            headings.append('start_time')
            headings.append('end_time')
            start_time, end_time, category = parallet_extract_time_category(tokens_data, 25)
            tokens_data['Category']=category
            tokens_data['start_time']=start_time 
            tokens_data['end_time']=end_time
            save_data_to_csv(headings, tokens_data, 'pinksale_launchpad.csv')
            print('total time taken: ', int(time.time()-t)//60, 'min', int(time.time()-t)%60, 'sec')
            print('------------------------------------------')
            time.sleep(1800-int(time.time()-t))

if __name__ == "__main__":
   ScrapeThread().start()