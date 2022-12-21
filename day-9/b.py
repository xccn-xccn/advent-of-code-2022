from sys import argv
from time import perf_counter

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


def single_move(head, tail):
    """Returns a tuple of the coordinates to add to tail (y,x)"""
    diff_y, diff_x = (head[0] - tail[0], head[1] - tail[1])
    if 1 >= diff_y >= -1 and 1 >= diff_x >= -1:
        return (0, 0)
    elif diff_y == 0:
        return (0, diff_x // abs(diff_x))
    elif diff_x == 0:
        return (diff_y // abs(diff_y), 0)
    return (diff_y // abs(diff_y), diff_x // abs(diff_x))


def main():  # cords are y,x
    instructions = {
        "U": (0, 1),
        "R": (1, 1),
        "D": (0, -1),
        "L": (1, -1),
    }  # index, amount
    been = set()
    been.add((0, 0))
    coords = [[0,0] for _ in range(10)]
    text = read_file(get_input_file()).splitlines()
    for i, line in enumerate(text):
        index, amount = instructions[line[0]]
        for instruction in range(int(line.split()[-1])):
            for current in range(9):
                head, tail = coords[current], coords[current + 1]
                if current == 0:
                    head[index] += amount
                move = single_move(head, tail)
                coords[current + 1][0], coords[current + 1][1] = coords[current + 1][0] + move[0], coords[current + 1][1] + move[1]
            been.add(tuple(coords[-1]))
    return len(been)


if __name__ == "__main__":
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')