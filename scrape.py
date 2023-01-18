from scrapper.pinksalelaunchpad import scrape_pinksale
from db_manager.pandas_save import save_data_to_csv
import time

while(True):
    time.sleep(1800)
    headings, tokens_data = scrape_pinksale()
    save_data_to_csv(headings, tokens_data, 'pinksale_launchpad.csv')