#   Read text input
#   Split the input using spaces and build Elves with list of calories
#   Sumarrize calories carried by each elf
#   Build a string with total calories per elf
#   Find the maximum value in the string

import re

input_file = "input_01.txt"

with open(input_file) as f:
    lines = f.readlines()

#print(lines)

class Elf:

    def __init__(self, id) -> None:
        self.id = id
        self.raw_input  = []
        self.calories = 0

    def add_calories(self, calories:str) -> None:
        self.raw_input.append(calories)
        #print(self.raw_input)
        #print(re.findall("\d*",calories)[0])
        self.calories += int(re.findall("\d*",calories)[0])

    def get_calories(self) -> int:
        return self.calories

    def get_id(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f'I am elf number {self.id} with {self.calories} calories.'


# Parse input
i = 0
elves = []

for line in lines:
    if line == '\n' or i == 0:
        # create a new elf
        i += 1
        new_elf = Elf(i)
        elves.append(new_elf)
        #print('New Elf number', str(i), new_elf)

    else:
        new_elf.add_calories(line)
        #print(i,line)

#print(*elves)

# Find elf with most calories

biggest_elf = 0
max_calories = 0

for elf in elves:
    #print(elf, elf.get_calories())
    if elf.get_calories() > max_calories:
        max_calories = elf.get_calories()
        biggest_elf = elf.get_id()

print(biggest_elf, max_calories)