# importing pandas as pd
import time
t = time.time()
import pandas as pd
print('time of loading pandas', time.time()-t)

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)

df.to_csv('file1.csv')

print(df)
print(time.time()-t)
print(time.time())