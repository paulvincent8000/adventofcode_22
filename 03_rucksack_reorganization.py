# Split the strings in half
# Find unique characters - sets
# Find common character in each set
# Test for upper or lower case
# Score the character and sum

#print(ord('a'))

#print('B'.isupper())

import functions as fn
import string

#for c in string.ascii_lowercase:
#    print(f'ASCII for {c} is {ord(c)-96}')

#for c in string.ascii_uppercase:
#    print(f'ASCII for {c} is {ord(c)-13}')

data = 'input_03.txt'

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
    
            # score the character
            if shared_character.isupper():
                ascii_offset = -38
            else:
                ascii_offset = -96
            score += ord(shared_character) + ascii_offset
            #print(setA, setB, shared_character, shared_character.isupper(), ord(shared_character)+ ascii_offset, score)

# output the result for part I
print(f'The sum of the priorities is {score}.')