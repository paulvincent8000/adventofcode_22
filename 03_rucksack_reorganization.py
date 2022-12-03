# Split the strings in half
# Find unique characters - sets
# Find common character in each set
# Test for upper or lower case
# Score the character and sum

#print(ord('a'))

#print('B'.isupper())

import functions as fn
import string

def score_character(character):
    if character.isupper():
        ascii_offset = -38
    else:
        ascii_offset = -96
    return ord(character) + ascii_offset

def get_common_characters(a,b) -> set:
    shared_character_set = set()
    for item in a:
        if item in b:
            shared_character_set.add(item)
    return shared_character_set

#for c in string.ascii_lowercase:
#    print(f'ASCII for {c} is {ord(c)-96}')

#for c in string.ascii_uppercase:
#    print(f'ASCII for {c} is {ord(c)-13}')

data = 'input_03.txt'
#data = 'input.txt'

lines = fn.Reader(data)
#print(f.get_lines())

score = 0

for line in lines.get_lines():
    length = len(line)
    index = int(length/2)
    first_compartment = line[:index]
    second_compartment = line[index:]
    #print(f'{length} {len(first_compartment)} {len(second_compartment)} {first_compartment} {second_compartment}' )

    # find unique characters in each compartment
    setA = set()
    for i in first_compartment:
        setA.add(i)

    setB = set()
    for i in second_compartment:
        setB.add(i)

    # find shared character in both compartments
    for i in setA:
        #print(f'{i} {setB} {i in setB}')
        if i in setB:
            shared_character = i
    
            score += score_character(i)
            #print(setA, setB, shared_character, shared_character.isupper(), ord(shared_character)+ ascii_offset, score)

# output the result for part I
#print(f'The sum of the priorities is {score}.')

# Part II

# build groups of three lines
line_number = 0
groups = []

for line in lines.get_lines():
    pos = line_number%3
    if pos == 0:
        group = [line]
    else:
        group.append(line)
    #print(line_number, pos, pos == 0, line, group, len(group))
    
    if len(group) == 3:
        groups.append(group)

    line_number += 1

# find and score common characters
score = 0
for group in groups:
    partial = get_common_characters(group[0],group[1])
    full = get_common_characters(partial,group[2])
    score += score_character(max(full))
    
    print(group, get_common_characters(group[0],group[1]), full, max(full), score_character(max(full)), score)

print(f'The score for part II is {score}')