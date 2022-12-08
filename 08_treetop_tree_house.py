import pandas as pd
import functions as fn

data = 'input.txt'
#data = 'input_08.txt'

trees = []
for line in fn.Reader(data).get_lines():
    trees.append([x for x in line])
    
df = pd.DataFrame(trees)


print(df)
#print(df.iloc[[1],[1]])
#print(df.iloc[:,1:3])
#print(df.iloc[0:3,1:5])

# pull a series and find the maximum value
#my_series = pd.Series( df.iloc[ : , 3] )
#print(my_series)
#print(type(my_series))
#print(my_series.max())
#print(my_series[:2])
#print(my_series[:2].max())

def is_visible(dataframe, row_nr, col_nr):
    loc = dataframe.iloc[ row_nr, col_nr ]
    row = pd.Series(dataframe.iloc[ row_nr  ])
    col = pd.Series(dataframe.iloc[ : , col_nr ])

    slice_left = row[:col_nr].max()
    slice_right = row[col_nr+1 : ].max()
    slice_above = col[:row_nr].max()
    slice_below = col[row_nr+1:].max()

    visible = slice_left < loc or slice_right < loc or slice_above < loc or slice_below < loc
    return visible

#test= is_visible(df, 2, 1)

#print(len(df.index), len(df.columns))

number_of_rows = len(df.index)
number_of_cols = len(df.columns)

visible_trees = 0
for row_nr in range(1,number_of_rows-1):
    for col_nr in range(1,number_of_cols-1):
        if is_visible(df, row_nr, col_nr):
            visible_trees += 1
        #print(f'row {row_nr} col {col_nr}, {visible_trees}')

outside_trees = 2 * number_of_rows + 2 * number_of_cols - 4

print(f'There are {visible_trees + outside_trees} visible trees.')