import time 
t = time.time()
import pandas as pd
print('time to import pandas', time.time()-t)
df = pd.read_csv('file1.csv')

print(df.to_string())
print(time.time()-t)