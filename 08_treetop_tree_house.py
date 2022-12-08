import pandas as pd
import functions as fn

data = 'input.txt'

trees = []
for line in fn.Reader(data).get_lines():
    trees.append([x for x in line])
    
df = pd.DataFrame(trees)

print(df)
print(df.iloc[[1],[1]])
print(df.iloc[:,1:3])
print(df.iloc[0:3,1:5])