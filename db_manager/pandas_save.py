import pandas as pd

def save_data_to_csv(heading, data, filename):
    df = pd.DataFrame(data, columns=heading)
    df.to_csv(filename)
