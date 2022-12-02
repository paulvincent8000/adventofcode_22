import functions as fn

#   get the throws
#   add throw score
#   check win or loss
#   add win or loss score

outcomes = {
    'A X'   :   3,  # rock / rock
    'A Y'   :   6,  # rock / paper
    'A Z'   :   0,  # rock / scissors
    'B X'   :   0,  # paper / rock
    'B Y'   :   3,  # paper / paper
    'B Z'   :   6,  # paper / scissors
    'C X'   :   6,  # scissors / rock
    'C Y'   :   0,  # scissors / paper
    'C Z'   :   3,  # scissors / scissors
}


throw_value = {
    'A X'   :   1,  # rock / rock
    'A Y'   :   2,  # rock / paper
    'A Z'   :   3,  # rock / scissors
    'B X'   :   1,  # paper / rock
    'B Y'   :   2,  # paper / paper
    'B Z'   :   3,  # paper / scissors
    'C X'   :   1,  # scissors / rock
    'C Y'   :   2,  # scissors / paper
    'C Z'   :   3,  # scissors / scissors
}

#data = 'input.txt'
data = 'input_02.txt'

throws = fn.Reader(data)
#print(throws.get_lines())

score = 0

for throw in throws.get_lines():
    score += throw_value[throw]
    score += outcomes[throw]
    print(throw, outcomes[throw], score)


#   PART II

throw2 = {
    'A X'   :   'A Z',  # rock / scissors
    'A Y'   :   'A X',  # rock / rock
    'A Z'   :   'A Y',  # rock / paper
    'B X'   :   'B X',  # paper / rock
    'B Y'   :   'B Y',  # paper / paper
    'B Z'   :   'B Z',  # paper / scissors
    'C X'   :   'C Y',  # scissors / paper
    'C Y'   :   'C Z',  # scissors / scissors
    'C Z'   :   'C X',  # scissors / rock
}

score = 0

for throw in throws.get_lines():
    score += throw_value[throw2[throw]]
    score += outcomes[throw2[throw]]
    print(throw, throw2[throw], throw_value[throw2[throw]], outcomes[throw2[throw]], score)