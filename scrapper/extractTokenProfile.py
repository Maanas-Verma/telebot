from bs4 import BeautifulSoup
def extract_time_and_category(title, table1, table2):
    start_time = ''
    end_time = ''
    category = ''
    soup = BeautifulSoup(table1, "html.parser")
    table_rows = soup.find_all('tr')
    for row in table_rows:
        row_data = row.find_all('td')
        if(len(row_data)<2):
            continue
        if('Start Time' in row_data[0].text):
            start_time = row_data[1].text
        if('End Time' in row_data[0].text):
            end_time = row_data[1].text
    if('Fair Launch' in title):
        category = 'Fair Launch'
    elif('Subscription' in title):
        category = 'Subscription'
    else:
        soup = BeautifulSoup(table2, "html.parser")
        table_rows = soup.find_all('tr')
        for row in table_rows:
            row_data = row.find_all('td')
            if(len(row_data)<2):
                continue
            if('Whitelist' in row_data[1].text):
                category = 'Whitelist'
            if('Public' in row_data[1].text):
                category = 'Public Presale'
    return start_time, end_time, category