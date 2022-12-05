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
        #print(line, len(line))
    return rows[-1].count('   ') + 1

def build_empty_stacks(number_of_stacks) -> list:
    stacks = []
    for i in range(number_of_stacks):
        stacks.append([])
    return stacks

def stack_crate(stacks, stack, crate) -> None:
    stacks[stack].append(crate)
    return

def parse_stack_lines(line) -> list:
    i = []
    for stack in range(1, len(line), 4):
        i.append(line[stack])
    return i


# build stacks as list
#print(stack_lines[2], parse_stack_lines(stack_lines[2]))

stacks = build_empty_stacks(get_number_of_stacks(stack_lines))

# Fill the stacks
for line in stack_lines:
    if line[1] == '1':
        continue
    parsed_line = parse_stack_lines(line)

    for stack in range(get_number_of_stacks(stack_lines)):
        if parsed_line[stack] == ' ':
            continue
        stack_crate(stacks, stack, parsed_line[stack])
        #print(stack, parsed_line[stack], parsed_line[stack] == ' ')

for stack in stacks:
    stack.reverse()

# print(stacks)
        

# get input for moves
# parse moves
# execute move
# find top container in stack