from sys import argv
from collections import deque


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def binary_search(arr, x):
    low, high, mid = 0, len(arr) - 1, 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low


def valid(grid, y, x, visited, special, current_letter):

    if not (0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y, x) not in visited):
        return False
    new_letter = grid[y][x]
    return ord(special.get(current_letter, current_letter)) + 1 >= ord(
        special.get(new_letter, new_letter)
    )


def get_length(grid, start, end):
    height, width = len(grid), len(grid[0])
    bag = deque([(start, 0)])  # [(pos, steps)]
    seen = {start}

    while bag:
        current, steps = bag.pop()
        cy, cx = current

        if current == end:
            return steps

        value = grid[cy][cx]
        for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
            pos = cy + dy, cx + dx
            py, px = pos
            if px < 0 or py < 0 or px >= width or py >= height or pos in seen:
                continue
            if grid[py][px] <= value + 1:
                bag.appendleft((pos, steps + 1))
                seen.add(pos)


def get_length2(grid, start, end):
    height, width = len(grid), len(grid[0])
    bag = deque([start])  # [pos]
    seen = {start: 0}

    while bag:
        current = bag.pop()
        cy, cx = current
        steps = seen[(current)]

        if current == end:
            return steps

        value = grid[cy][cx]
        for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
            pos = cy + dy, cx + dx
            py, px = pos
            if px < 0 or py < 0 or px >= width or py >= height or pos in seen:
                continue
            if grid[py][px] <= value + 1:
                bag.appendleft(pos)
                seen[pos] = steps + 1


def get_length3(grid, start, end):
    height, width = len(grid), len(grid[0])
    seen = {start}

    bag = [start]

    steps = 0
    while True:
        next_bag = []

        for current in bag:
            cy, cx = current

            if current == end:
                return steps

            value = grid[cy][cx]
            for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
                pos = cy + dy, cx + dx
                py, px = pos
                if px < 0 or py < 0 or px >= width or py >= height or pos in seen:
                    continue
                if grid[py][px] <= value + 1:
                    next_bag.append(pos)
                    seen.add(pos)
        bag = next_bag
        steps += 1


def get_length_c(grid, start, end):
    bag = deque([(start, 0)])  # [(pos, steps)]
    seen = {start}

    while bag:
        current, steps = bag.pop()

        if current == end:
            return steps

        value = grid[current]
        for dp in 1, -1, 1j, -1j:
            pos = current + dp
            if pos in seen:
                continue
            if grid.get(pos, float("inf")) <= value + 1:
                bag.appendleft((pos, steps + 1))
                seen.add(pos)


def main():
    grid = list(map(list,read_file(get_input_file()).splitlines(),
        )
    )
    print(grid)
    complex_grid = {}
    for y, line in enumerate(grid):
        for x, square in enumerate(line):
            pos = x + 1j * y
            if square == "S":
                square = "a"
                start = pos
            elif square == "E":
                square = "z"
                end = pos
            complex_grid[pos] = ord(square)

    print(complex_grid)
    return get_length_c(complex_grid, start, end)


# def main():
#     grid = list(
#         map(
#             lambda line: [ord(x) for x in line],
#             read_file(get_input_file()).splitlines(),
#         )
#     )
#     print(grid)
#     for y, line in enumerate(grid):
#         for x, square in enumerate(line):
#             if square == ord("S"):
#                 grid[y][x] = ord("a")
#                 start = (y, x)
#             elif square == ord("E"):
#                 grid[y][x] = ord("z")
#                 end = (y, x)

#     return get_length3(grid, start, end)


if __name__ == "__main__":
    print(main())
