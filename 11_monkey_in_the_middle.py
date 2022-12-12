# imports
import functions as fn

# get the input data
input_file = 'sample_input_11.txt'
#input_file = 'input_11.txt'

lines = fn.Reader(input_file).get_lines()

# classes
class Monkey():

    def __init__(self, input:str) -> None:
        self.input = input
        self.name = input[0].replace(' ','_')[:-1]
        self.itemsx = input[1][18:].split(',')
        self.items = []
        for item in self.itemsx:
            self.items.append(int(item))
        self.old = 0
        self.factor = 0
        self.new = 0
        self.divisor = int(input[3][-2:])
        self.monkey_true = 'Monkey_'+input[4][29:]
        self.monkey_false = 'Monkey_'+input[5][30:]
        self.inspections = 0
#        print('Monkey_'+input[5][30:], self.name)

    def operation(self) -> None:
        self.old = self.items.pop(0)
        self.inspections += 1
        if self.input[2][25:] == 'old':
            self.factor = self.old
        else:
            self.factor = int(self.input[2][25:])
        if self.input[2][23] == '+':
            self.new = self.old + self.factor
        elif self.input[2][23] == '*':
            self.new = self.old * self.factor
        elif self.input[2][23] == '-':
            self.new = self.old - self.factor
        elif self.input[2][23] == '/':
            self.new = self.old / self.factor
#        self.adjusted_worry_level = int(self.new/3)
        self.adjusted_worry_level = self.new
        #print(f'{self.name}, {self.factor}, {self.old}, {self.adjusted_worry_level})
        return self.adjusted_worry_level

    def has_items(self) -> bool:
        return len(self.items)  > 0

    def select_monkey_to_throw(self):
        if self.adjusted_worry_level % self.divisor == 0:
            return self.monkey_true
        else:
            return self.monkey_false
#        return self.adjusted_worry_level % self.divisor == 0

    def catch_item(self, item):
        self.items.append(item)

    def get_inspections(self):
        return self.inspections

    def __str__(self) -> str:
        return f'I am {self.name}!'

# build monkeys
monkeys = {}
monkey_input = []
for line in lines:
    monkey_input.append(line)
    if len(line)==0:
        key = (monkey_input[0].replace(' ','_')).replace(':','')
        value = monkey_input
        monkeys[key] = Monkey(value)
        monkey_input = []

#print(monkeys['Monkey_1'], monkeys['Monkey_1'].has_items())

for round in range(1000):
    for monkey in monkeys:
        while monkeys[monkey].has_items():
            item = monkeys[monkey].operation()
            to = monkeys[monkey].select_monkey_to_throw()
            monkeys[to].catch_item(item)
            #print(monkey,to, item)
    print(f'Round {round}')

inspections = []            
for monkey in monkeys:
    inspections.append(monkeys[monkey].inspections)
    #print(monkeys[monkey].items, monkeys[monkey].inspections)

print(inspections, inspections.sort(reverse=True))

print(inspections[0] * inspections[1])