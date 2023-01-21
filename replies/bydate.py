import pandas as pd
from datetime import datetime, timezone
from datetime import timedelta

def get_tokens_by_date(date):
    df = pd.read_csv('pinksale_launchpad.csv')
    selected_tokens = df[df.filter(['start_time']).start_time.str.contains(date)][['Name', 'telegram']]
    tokens_dict = selected_tokens.to_dict()
    output = ""
    for ele in tokens_dict['Name'].keys():
        if type(tokens_dict['telegram'][ele]) == 'str':
            output += tokens_dict['Name'][ele] + " - [\U0001F4AC]("+ tokens_dict['telegram'][ele]+") "  + "\n"
        else:
            output += tokens_dict['Name'][ele] + "\n"
    return output

def get_tomorrows_tokens(count):
    tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
    tomorrow = tomorrow.strftime('%Y.%m.%d')
    return get_tokens_by_date(tomorrow)

def get_todays_tokens(count):
    today = datetime.now(timezone.utc).strftime('%Y.%m.%d')
    return get_tokens_by_date(today)
    
def get_later_tokens(count):
    pass 

def get_3days_tokens(count):
    pass

if __name__=='__main__':
    get_tomorrows_tokens()