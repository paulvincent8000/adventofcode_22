import functions as fn

# get input for stacks
stack_data = 'inputa.txt'
#stack_data = 'input_05a.txt'
stack_lines = fn.Reader(stack_data).get_lines()

# find the number of stacks
def get_number_of_stacks(lines) -> int:
    rows = []
    for line in lines:
        rows.append(line)
    return rows[-1].count('   ') + 1
print(get_number_of_stacks(stack_lines))

# build stacks as lists



# get input for moves
# parse moves
# execute move
# find top container in stack