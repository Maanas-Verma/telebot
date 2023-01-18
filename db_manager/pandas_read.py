import pandas as pd

def get_validated_tokens(validity):
    df = pd.read_csv('pinksale_launchpad.csv')
    valid_tokens = df[df[validity] == True][['Name', 'telegram']]
    values = valid_tokens.to_dict()
    output = ""
    for ele in values['Name'].keys():
        output += values['Name'][ele] + " - [\U0001F4AC]("+ values['telegram'][ele]+") "  + "\n"
    return output

if __name__ == '__main__':
    print(get_validated_tokens())