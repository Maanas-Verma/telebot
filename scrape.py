from scrapper.pinksalelaunchpad import scrape_pinksale
from db_manager.pandas_save import save_data_to_csv
# from scrapper.extractTokenProfile import extractCategory
import time

while(True):
    headings, tokens_data = scrape_pinksale()
    # headings.append('Category')
    # headings.append('start time')
    # headings.append('end time')
    # extractCategory(tokens_data)
    save_data_to_csv(headings, tokens_data, 'pinksale_launchpad.csv')
    print('first done')
    time.sleep(1800)