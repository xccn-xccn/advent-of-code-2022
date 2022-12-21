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


def main():
    instructions = read_file(get_input_file()).splitlines()
    cycles, x, strength, interesting = 0, 1, 0, [20, 60, 100, 140, 180, 220]
    for line in instructions:
        if (cycles + 1) % 40 == 20:
            strength += x * (cycles + 1)
        if line[0] == "n":
            cycles += 1
        elif line[0] == "a":
            if (cycles + 2) % 40 == 20:
                strength += x * (cycles + 2)
            cycles += 2
            x += int(line.split()[-1])
    return strength


if __name__ == "__main__":
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
