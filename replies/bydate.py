import pandas as pd
from datetime import datetime, timezone
from datetime import timedelta

def formated_print(df, taxesdf, count):
    tokens_dict = df.to_dict()
    output = ""
    for ele in tokens_dict['Name'].keys():
        output += "``` "+tokens_dict['start_time'][ele].split(' ')[1] + "|"
        if(tokens_dict['Category'][ele] == 'Public Presale'):
            output += 'PU'
        elif(tokens_dict['Category'][ele] == 'Fair Launch'):
            output += 'FL'
        elif(tokens_dict['Category'][ele] == 'Whitelist'):
            output += 'WL'
        else:
            output += 'SB'
        # get taxes

        token_taxes = taxesdf[taxesdf['Name'] == tokens_dict['Name'][ele]]
        if(not token_taxes.empty):
            output += "|" + str(token_taxes['buy_tax'].values[0]) + "/" + str(token_taxes['sell_tax'].values[0])

        output += "|``` [\U0001F4F2]("+ tokens_dict['twitter'][ele]+") "
        output += " [\U0001F310]("+ tokens_dict['website'][ele]+") |"
        if isinstance(tokens_dict['telegram'][ele], str):
            output += " [" + tokens_dict['Name'][ele] + "](" + tokens_dict['telegram'][ele] + ")\n"
        else:
            output += tokens_dict['Name'][ele] + "\n"
        count-=1
        if(count==0): break
    return output

def get_tokens_by_date(date, count):
    df = pd.read_csv('pinksale_launchpad.csv')
    taxesdf = pd.read_csv('taxes.csv')
    selected_tokens = df[df.filter(['start_time']).start_time.str.contains(date)][['Name', 'telegram','start_time','twitter', 'website', 'Category']]
    output = formated_print(selected_tokens, taxesdf, count)
    if(output==""):
        output = "No tokens found for " + date + "\n"
    return output

def get_tomorrows_tokens(count):
    tomorrow = (datetime.now(timezone.utc) + timedelta(days=1)).strftime('%Y.%m.%d')
    output = "Tomorrow's (" + (datetime.now(timezone.utc) + timedelta(days=1)).strftime('%d/%m') + ") tokens are:\nTimes are in UTC \n \n"
    return output + get_tokens_by_date(tomorrow, count)

def get_todays_tokens(count):
    today = datetime.now(timezone.utc).strftime('%Y.%m.%d')
    output = "Today's (" + datetime.now(timezone.utc).strftime('%d/%m') + ") tokens are:\nTimes are in UTC \n \n"
    return output + get_tokens_by_date(today, count)
    
def get_later_tokens():
    plus4day = datetime.now(timezone.utc) + timedelta(days=1)
    plus5day = datetime.now(timezone.utc) + timedelta(days=2)
    plus6day = datetime.now(timezone.utc) + timedelta(days=3)

    data = "later three days \n(" + plus4day.strftime('%d/%m') + "-" 
    data = data + plus6day.strftime('%d/%m') + ") tokens are: \nTimes are in UTC \n "

    data = data + "\n " + plus4day.strftime('%d/%m') + " \n"
    data = data + get_tokens_by_date(plus4day.strftime('%Y.%m.%d'), 2)

    data = data + "\n " + plus5day.strftime('%d/%m') + " \n"
    data = data + get_tokens_by_date(plus5day.strftime('%Y.%m.%d'), 2)

    data = data + "\n " + plus6day.strftime('%d/%m') + " \n"
    data = data + get_tokens_by_date(plus6day.strftime('%Y.%m.%d'), 2)

    return data

def get_3days_tokens():
    plus1day = datetime.now(timezone.utc) + timedelta(days=1)
    plus2day = datetime.now(timezone.utc) + timedelta(days=2)
    plus3day = datetime.now(timezone.utc) + timedelta(days=3)
    
    data = "Next three days \n(" + plus1day.strftime('%d/%m') + "-" 
    data = data + plus3day.strftime('%d/%m') + ") tokens are: \nTimes are in UTC \n "

    data = data + "\n(" + plus1day.strftime('%d/%m') + ") \n"
    data = data + get_tokens_by_date(plus1day.strftime('%Y.%m.%d'), 2)
    
    data = data + "\n(" + plus2day.strftime('%d/%m') + ") \n"
    data = data + get_tokens_by_date(plus2day.strftime('%Y.%m.%d'), 2)

    data = data + "\n(" + plus3day.strftime('%d/%m') + ") \n"
    data = data + get_tokens_by_date(plus3day.strftime('%Y.%m.%d'), 2)

    return data

if __name__=='__main__':
    get_tomorrows_tokens()