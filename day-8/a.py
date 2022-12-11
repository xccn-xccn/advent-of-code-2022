from sys import argv


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def can_see(square):
    seen = set()
    for y_index, row in enumerate(square):
        for seen_x in can_see_line(row, y_index):
            seen.add((seen_x, y_index))
    for x_index in range(len(square)):
        column = []
        for y_index, row in enumerate(square):
            column.append(row[x_index])
        for seen_y in can_see_line(column):
            seen.add((x_index, seen_y))

    return seen


def can_see_line(line):
    seen = set()
    for iteration in range(2):
        tallest = -1
        for x_index, tree in enumerate(line):
            if tree > tallest:
                seen.add(x_index if iteration == 0 else len(line) - x_index - 1)
                tallest = tree
        line.reverse()
    return seen


def main():
    seen = set()
    text = [list(map(int, line)) for line in read_file(get_input_file()).splitlines()]
    seen = can_see(text)
    return len(seen)


if __name__ == "__main__":
    print(main())
