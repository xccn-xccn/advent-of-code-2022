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


def add_to_image(image, cycle, sprite_x):
    image[cycle // 40].append(
        "\u25A0"
        if len(image[cycle // 40]) in (sprite_x - 1, sprite_x, sprite_x + 1)
        else " "
    )
    return image


def main():
    instructions = read_file(get_input_file()).splitlines()
    cycle, sprite_x, image, = (
        0,
        1,
        [[] for x in range(6)],
    )
    for line in instructions:
        if line[0] == "n":
            image = add_to_image(image, cycle, sprite_x)
            cycle += 1
        elif line[0] == "a":
            for _ in range(2):
                image = add_to_image(image, cycle, sprite_x)
                cycle += 1
            sprite_x += int(line.split()[-1])
    return image


if __name__ == "__main__":
    for line in main():
        print("".join(line))
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
