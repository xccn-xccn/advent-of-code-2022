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


# from enum import Enum, auto

# class Comparison(Enum):
#     Lower = auto()
#     Equal = auto()
#     Greater = auto()


# def format_input(input, output=None):  #
#     print(output)
#     # print(input, "input is")
#     ending_bracket = -1
#     if output == None:
#         output = []
#     for i, char in enumerate(input):
#         # print(input, "input in loop")
#         if i < ending_bracket:
#             continue
#         elif char == "[":
#             # print(input[i:])
#             ending_bracket = find_match(input[i:]) + i
#             # print(ending_bracket,'ending bracket')
#             # if ending_bracket == None:
#             # print("ending bracket == None", input[i:])
#             # print('next output input is',input[i + 1 : ending_bracket],input,i+1,ending_bracket,input[:-1].rfind(']'))
#             output.append(
#                 format_input(input[i + 1 : ending_bracket], output=deepcopy(output))
#             )
#         elif char.isdigit():  # else
#             output.append(int(char))
#     # print(output)
#     return list(output)


def find_match(input):
    """Return index of matching bracket pair.
    Input must be valid parenthesis."""
    count = 0
    for i, item in enumerate(input):
        if item == "[":
            count += 1
        elif item == "]":
            count -= 1
            if count == 0:
                return i


def xor(first, second):
    return bool(first) != bool(second)


def correct_single(first, second):
    pass


def format_input1(input):
    output = []
    while "[" in input:
        beginning = input.rfind("[")
        end = input.find("]")
        c_value = input[beginning + 1 : end]
        input = input[:beginning] + input[end:]
        for item in c_value:
            if item == ",":
                continue
            output.append(item)
        output = [output]
    return output[0]


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
        if isinstance(first_value, str) or isinstance(second_value, str):
            if xor(first_value == 'last item', second_value == 'last item'):
                    return 1 if first_value == 'last item' else 3
        elif isinstance(first_value, int) and isinstance(second_value, int):
            result = compare(first_value, second_value)
            if result != 2:
                return result
        elif isinstance(first_value, list) and isinstance(second_value, list):
            result = correct_pair((first_value, second_value))
            if result != 2:
                return result
        else:
            result = (
                correct_pair([first_value, [second_value]])
                if isinstance(first_value, list)
                else correct_pair([[first_value], second_value])
            )
            if result != 2:
                return result
    return 2


def format_input2(input):
    output = []
    for i, line in enumerate(input):
        if i % 2 == 0:
            output.append([])
        output[-1].append(eval(line))
    return output


def main():  # use the thing from day 7
    text = read_file(get_input_file()).split()
    f_text = format_input2(text)
    correct_count = 0
    for i, pair in enumerate(f_text, 1):
        result = correct_pair(pair)
        if result == 1:
            correct_count += i
    return correct_count


if __name__ == "__main__":
    print(main())
    pass
