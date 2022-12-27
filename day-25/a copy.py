from sys import argv
from time import perf_counter


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def padd(alist, n):
    return ["0"] * (n) + list(alist)


def add(num1, num2):
    """Input should be list of strings or strings"""
    new = []
    extra = 0
    convert = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2,
        2: "2",
        1: "1",
        0: "0",
        -1: "-",
        -2: "=",
    }
    if len(num1) > len(num2):
        num2 = padd(num2, len(num1) - len(num2))
    else:
        num1 = padd(num1, len(num2) - len(num1))
    for n1, n2 in zip(num1[::-1], num2[::-1]):
        number = convert[n1] + convert[n2] + extra
        if number > 2:
            new.append(convert[number - 5])
            extra = 1
        elif number < -2:
            extra = -1
            new.append(convert[number + 5])
        else:
            new.append(convert[number])
            extra = 0
    if extra:
        new.append("1")
    return list(reversed(new))


def main():  # solves by summing in snafu
    text = read_file(get_input_file()).splitlines()
    current = []
    for line in text:
        current = add(current, list(line))
    return "".join(current)


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
