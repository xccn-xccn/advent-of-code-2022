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


def xor(first, second):
    return bool(first) != bool(second)


def correct_single(first, second):
    if isinstance(first, str) or isinstance(second, str):
        if xor(first == 'last item', second == 'last item'):
                return 1 if first == 'last item' else 3
    elif isinstance(first, int) and isinstance(second, int):
        result = compare(first, second)
        if result != 2:
            return result
    elif isinstance(first, list) and isinstance(second, list):
        result = correct_pair((first, second))
        if result != 2:
            return result
    else:
        result = (
            correct_pair([first, [second]])
            if isinstance(first, list)
            else correct_pair([[first], second])
        )
        if result != 2:
            return result


def compare(first, second):
    if first == second:
        return 2
    return 1 if first < second else 3


def correct_pair(pair):  # 1,2,3 yes draw no
    first, second = pair
    if isinstance(first, int):
        first = [first]
    if isinstance(second, int):
        second = [second]
    first.append('last item')
    second.append('last item')
    for first_value, second_value, i in zip(first, second, range(len(first))):
        result = correct_single(first_value, second_value)
        if result == 2:
            continue
        return result
    return 2


def format_input(input):
    output = []
    for line in input:
        output.append(eval(line))
    return output


def main():
    text = read_file(get_input_file()).split()
    f_text = format_input(text)
    count2 = 1
    count6 = 2
    for i, pair in enumerate(f_text, 1):
        result = correct_pair((pair,[[2]]))
        if result == 1:
            count2 += 1
        result = correct_pair((pair,[[6]]))
        if result == 1:
            count6 += 1
    return count2 * count6


if __name__ == "__main__":
    print(main())
    pass
