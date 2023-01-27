import pandas as pd

def add_tax(txt):
    if(txt.split(' ')[0] != "/addtax"):
        return "Invalid command"
    elif(len(txt.split(' ')) < 4):
        return "Please provide in the format \ntoken\_name buy\_tax sell\_tax \neg: /addtax PINK 10 10"
    token_name = ''
    for i in range(1, len(txt.split(' ')) - 2):
        token_name += txt.split(' ')[i] + ' '
    token_name = token_name.strip()
    print(token_name)
    buy_tax = txt.split(' ')[-2]
    sell_tax = txt.split(' ')[-1]

    # validate token name
    tokens_data = pd.read_csv('pinksale_launchpad.csv')
    if(tokens_data[tokens_data['Name'] == token_name].empty):
        return "Token not found"

    if(not buy_tax.isdigit() or not sell_tax.isdigit()):
        return "Please provide in the format \ntoken\_name buy\_tax sell\_tax \neg: /addtax PINK 10 10"
    df = pd.read_csv('taxes.csv')
    if(df[df['Name'] == token_name].empty):
        df = df.append({'Name': token_name, 'buy_tax': buy_tax, 'sell_tax': sell_tax}, ignore_index=True)
        df.to_csv('taxes.csv', index=False)
        return "Tax added successfully"
    else:
        # update
        df.loc[df['Name'] == token_name, 'buy_tax'] = buy_tax
        df.loc[df['Name'] == token_name, 'sell_tax'] = sell_tax
        df.to_csv('taxes.csv', index=False)
        return "Tax updated successfully"