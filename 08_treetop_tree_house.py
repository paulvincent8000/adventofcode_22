import pandas as pd
import functions as fn

#data = 'input.txt'
data = 'input_08.txt'

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

# part II

def get_scenic_score(dataframe, row_nr, col_nr):
    loc = dataframe.iloc[ row_nr, col_nr ]
    row = pd.Series(dataframe.iloc[ row_nr  ])
    col = pd.Series(dataframe.iloc[ : , col_nr ])

    slice_left = row[:col_nr]
    slice_right = row[col_nr+1 : ]
    slice_above = col[:row_nr]
    slice_below = col[row_nr+1:]

    scenic_score_left = 0
    for slice in reversed(slice_left):
        scenic_score_left += 1
        if slice >= loc:
            break

    scenic_score_above = 0
    for slice in reversed(slice_above):
        scenic_score_above += 1
        if slice >= loc:
            break

    scenic_score_right = 0
    for slice in slice_right:
        scenic_score_right += 1
        if slice >= loc:
            break

    scenic_score_below = 0
    for slice in slice_below:
        scenic_score_below += 1
        if slice >= loc:            
            break
    #print(f'below: {scenic_score_below}, right: {scenic_score_right}, above: {scenic_score_above}, left: {scenic_score_left}')

    return scenic_score_left * scenic_score_above * scenic_score_below * scenic_score_right

#test = get_scenic_score(df, 3, 2)
#print(test)

scenic_scores = []
for row_nr in range(0,number_of_rows):
    for col_nr in range(0,number_of_cols):
        scenic_scores.append(get_scenic_score(df, row_nr, col_nr))
        #print(row_nr,col_nr)
#print(scenic_scores, max(scenic_scores))

print(f'The highest possible scenic score is {max(scenic_scores)}')