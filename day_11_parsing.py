from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list #[int]
    operation: str
    test: int
    target: tuple #[int, int]


def parse_input(input) -> list:
    monkeys = []

    monkeys_string = [monkey.strip() for monkey in input.split("\n\n")]
    #return monkeys_string
    #return monkeys_string[0]
    #return monkeys_string[0].split("\n")

    for m in monkeys_string:
        
        name, items, operation, test, if_true, if_false = [
            line.strip() for line in m.split("\n")
        ]
        items = deque([int(item.strip()) for item in items[16:].split(",")])
        operation = operation.split("=")[-1].strip()
        test = int(test.split(" ")[-1])
        if_true = int(if_true.split(" ")[-1])
        if_false = int(if_false.split(" ")[-1])
        target = (if_false, if_true)

        monkeys.append(Monkey(items, operation, test, target))
    return monkeys




if __name__ == "__main__":
    with open("sample_input_11.txt", "r", encoding="utf-8") as puzzle_input:
        monkeys_string = puzzle_input.read()

    monkeys = parse_input(monkeys_string)

    print(monkeys)