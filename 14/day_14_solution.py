# IMPORT
# ----------------------------------------------------------------------------
import os
import sys
# get path to directory where this file is present
current = os.path.dirname(os.path.realpath(__file__))
# get path to parent directory where this directory is present
parent = os.path.dirname(current)
# add parent directory to sys.path
sys.path.append(parent)
# import the module
import functions as fn
import pandas as pd

# CLASSES
# ----------------------------------------------------------------------------

# FUNCTIONS
# ----------------------------------------------------------------------------
def parse_line(line) -> list:
    '''Returns nested list [ [x1,y1], [x2,y2],... ]'''
    coordinates = []
    for i in [ a for a in line.split('->')]:
        coordinates.append( [ int(b) for b in i.strip().split(',') ] )
    return coordinates

def get_coordinate_range(lines) -> list:
    '''Returns x min, x max, y min and y max coordinates.'''
    # find min and max values for x and y coordinates
    xmin = 500
    xmax = 500
    ymin = 0
    ymax = 0
    for line in lines:
        xline = [ x[0] for x in  parse_line(line) ] 
        #print(  xline, min(xline), max(xline)  )
        if min(xline) < xmin:
            xmin = min(xline)
        if max(xline) > xmax:
            xmax = max(xline)
        #print(  xline, xmin, xmax  )
        yline = [ x[1] for x in  parse_line(line) ] 
        if max(yline) > ymax:
            ymax = max(yline)
        #print( yline, ymax )
    return [xmin, xmax, ymin, ymax]

# EXECUTE
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    
    # get input data
    data = "sample_input.txt"
    #data = "full_input.txt"
    lines = fn.Reader(current+"/"+data).get_lines()
    
    # get x and y headers and build empty dataframe
    rangex = [x for x in range(get_coordinate_range(lines)[1]+1) if x >= get_coordinate_range(lines)[0]]
    rangey = [x for x in range(get_coordinate_range(lines)[3]+1)]
    df = pd.DataFrame(index=rangey, columns=rangex)
    #print(df)

    print( df.iloc[497] )