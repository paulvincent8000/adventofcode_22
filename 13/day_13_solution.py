# IMPORT
# ----------------------------------------------------------------------------
import json

# CLASSES
# ----------------------------------------------------------------------------

# FUNCTIONS
# ----------------------------------------------------------------------------

def get_pairs(input:str) -> dict:
    pairs = {}
    i = 0
    for pair in input.split("\n\n"):
        padded = pair.replace('[]', '999')
        i += 1
        pairs[i] = padded.split("\n")
    return pairs

def parse_signal(signal:str):

    stack_level = 0
    stack = ['']
    for char in signal:
        if char == '[':
            stack_level += 1
            stack.append('')
        elif char ==']':
            stack[stack_level-1] += stack[stack_level]
            stack_level -= 1
        else:
            stack[stack_level] += char
        print(stack_level, char)
    return stack[0]
#    return [int(x) for x in array[0] if x != ',']

# compare data types and convert as needed
# flag not valid if right side is ever smaller and break the loop

# EXECUTE
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    
    #input_file = "/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_22/13/sample_input.txt"
    input_file = "sample_input.txt"
    with open(input_file, "r", encoding="utf-8") as puzzle_input:
        pairs_string = puzzle_input.read()

    pairs = get_pairs(pairs_string)

    
    test = [1,
                [12
                ]            
            ]
    print(parse_signal('999,[8,6,[6,3,[6,10,10,9],[8]]],[1,[1],4]]'))
    #print(parse_signal('[1,[2,[3,[4,[5,6,7]]]],8,9]'))