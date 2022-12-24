from sys import argv
from time import perf_counter
import re


start = perf_counter()


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def single_info(monkey_info):
    info = []
    for i, line in enumerate(monkey_info.splitlines()[1:]):
        if i == 1:
            operator = re.search("[\+*]", line).group(0)
            number = re.search("[0-9]+", line)
            if number:
                info.append(operator + number.group(0))
            else:
                info.append("**")  # square
        elif i in [2, 3, 4]:
            info.append(int(re.search("[0-9]+", line).group(0)))
        else:
            info.append([int(x) for x in re.findall("[0-9]+", line)])
    info.append(0)
    return info


def format_input1(notes):
    return [
        [int(num) for num in monkey.splitlines()[1][18:].split(",")]
        for i, monkey in enumerate(notes)
    ]


def calculate(value, equation):
    operator = re.search("[\+*]", equation).group(0)
    number = re.search("[0-9]+", equation)
    return eval(f"{value} {operator} {number.group(0) if number else value}") // 3


def single_monkey(notes):
    yes, no = [], []
    for item in notes[0]:
        value = calculate(item, notes[1])
        if value % notes[2] == 0:
            yes.append(value)
        else:
            no.append(value)
    return yes, no


def main():
    notes = read_file(get_input_file()).split("\n\n")
    monkeys = []
    for note in notes:
        monkeys.append(single_info(note))
    for repeat in range(20):
        for notes in monkeys:
            notes[-1] += len(notes[0])
            yes, no = single_monkey(notes)
            monkeys[notes[3]][0].extend(yes)
            monkeys[notes[4]][0].extend(no)
            notes[0].clear()
    most_items = sorted([line[-1] for line in monkeys])[-2:]
    return most_items[0] * most_items[1]


if __name__ == "__main__":
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
