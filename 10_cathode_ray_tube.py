import functions as fn

# start value = 1
# noop takes one cycle
# add x add value x and is effective after 2 further cycles

# find number of cycles at each step
# find cumulative value of signal at each cycle

# Find the signal strength during the 
# 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
# What is the sum of these six signal strengths?

# noop          1       1
# addx 3        2       1
#               3       4
# addx -5       4       4
#               5       -1

data = 'input.txt'

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



print(parse_instruction(instructions[2]))
