import pandas as pd
from datetime import datetime, timezone
from datetime import timedelta

def get_tokens_by_date(date, count):
    df = pd.read_csv('pinksale_launchpad.csv')
    selected_tokens = df[df.filter(['start_time']).start_time.str.contains(date)][['Name', 'telegram']]
    tokens_dict = selected_tokens.to_dict()
    output = ""
    for ele in tokens_dict['Name'].keys():
        if type(tokens_dict['telegram'][ele]) == 'str':
            output += tokens_dict['Name'][ele] + " - [\U0001F4AC]("+ tokens_dict['telegram'][ele]+") "  + "\n"
        else:
            output += tokens_dict['Name'][ele] + "\n"
        count-=1
        if(count==0): break
    return output

def get_tomorrows_tokens(count):
    tomorrow = (datetime.now(timezone.utc) + timedelta(days=1)).strftime('%Y.%m.%d')
    return get_tokens_by_date(tomorrow, count)

def get_todays_tokens(count):
    today = datetime.now(timezone.utc).strftime('%Y.%m.%d')
    return get_tokens_by_date(today, count)
    
def get_later_tokens():

    data = ""
    plus4day = (datetime.now(timezone.utc) + timedelta(days=4)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(plus4day, 2)

    plus5day = (datetime.now(timezone.utc) + timedelta(days=5)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(plus5day, 2)

    plus6day = (datetime.now(timezone.utc) + timedelta(days=6)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(plus6day, 2)

    return data

def get_3days_tokens():
    
    data = ""
    tomorrow = (datetime.now(timezone.utc) + timedelta(days=1)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(tomorrow, 2)

    day_after_tomorrow = (datetime.now(timezone.utc) + timedelta(days=2)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(day_after_tomorrow, 2)

    day_after_day_after_tomorrow = (datetime.now(timezone.utc) + timedelta(days=3)).strftime('%Y.%m.%d')
    data = data + get_tokens_by_date(day_after_day_after_tomorrow, 2)

    return data

if __name__=='__main__':
    get_tomorrows_tokens()