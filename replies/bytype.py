import pandas as pd
from replies.bydate import formated_print

def get_tokens_by_category(validity):
    df = pd.read_csv('pinksale_launchpad.csv')
    taxesdf = pd.read_csv('taxes.csv')
    valid_tokens = df[df[validity] == True][['Name', 'telegram','start_time','twitter', 'website', 'Category']]
    output = formated_print(valid_tokens, taxesdf, 5)
    if(output==""):
        output = "No tokens found for " + validity + " category\n"
    output = "Tokens in " + validity + " category are:\n\n" + output

    return output