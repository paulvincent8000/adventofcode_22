import functions as fn
import re

# get input for stacks
#stack_data = 'inputa.txt'
stack_data = 'input_05a.txt'
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

def remove_crate(stacks, stack) -> str:
    return stacks[stack].pop()

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

#print(stacks)
        
#=========================================

move_data = 'input_05b.txt'
#move_data = 'inputb.txt'

move_lines = fn.Reader(move_data)

for line in move_lines.get_lines():
    parse_move = re.findall('\d+', line)
    number_of_containers = int(parse_move[0])
    from_stack = int(parse_move[1])-1
    to_stack = int(parse_move[2])-1
    #print(line, parse_move ,number_of_containers, from_stack, to_stack)

    for movement in range(number_of_containers):
        crate = remove_crate(stacks, from_stack)
        stack_crate(stacks, to_stack, crate)

#print(stacks, from_stack, to_stack, number_of_containers, crate)

top_crates = []
for stack in stacks:
    top_crates.append(stack.pop())
print(top_crates)

# Part II
# =================================