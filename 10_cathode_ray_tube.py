import functions as fn
import pandas as pd

#data = 'input.txt'
data = 'input_10.txt'

instructions = fn.Reader(data).get_lines()

execution_cycles = {
    'noop'  : 1  ,
    'addx'  : 2
}

def parse_instruction(instruction:str) -> tuple:
    '''Output operation, value, cycles'''
    operation = instruction.split(' ')[0]
    if operation != 'noop':
        value = int(instruction.split(' ')[1])
    else:
        value = 0
    cycles = execution_cycles[operation]
    return (operation, value, cycles)

def get_operations(operation:tuple) -> pd.DataFrame:
    operation_set = []
    for i in range(operation[2]):
        if i == operation[2]-1:
            operation_set.append( {'instruction' : operation[0], 'value' : operation[1], 'cycles' : 1 } )
        else:
            operation_set.append( {'instruction' : operation[0], 'value' : 0, 'cycles' : 1 } )
    new_operation = pd.DataFrame(operation_set)
        
    return new_operation

#print(get_operations(('addx', 3, 2)))    

data = [['noop', 1, 1]]
col = ['instruction','value','cycles']
df = pd.DataFrame(columns=col, data=data)

# build dataframe with instructions per cycle
for instruction in instructions:
    next_instruction = parse_instruction(instruction)
    next_operation = get_operations(next_instruction)

    #print(next_operation)

    #df = df = df.append([{'instruction':'new', 'value':25, 'cycles':'40'}], ignore_index=True)
    df = pd.concat([df, next_operation], axis=0, ignore_index=True)

# calculate signal strength
df['signal'] = df['value'].cumsum()
df['total cycles'] = df['cycles'].cumsum()

#print(df.iloc[0:20])

# get signal strength at specific cycle
#print(df.iloc[[20,60,100,140,180,220],:])

df = df.iloc[[19,59,99,139,179,219],:]

df['signal strength'] = df['signal'] * df['total cycles']

df['answer'] = df['signal strength'].cumsum()
print(df)

