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


def right(pair):
    first, second = pair
    first_value, second_value = first[0], second[0]
    if isinstance(first_value, int) and isinstance(second_value, int):
        if first == second:
            if len(first) == 1 or len(second) == 1:
                return len(first) == 1
            return right((first[1:], second[1:]))
        return first < second
    elif isinstance(first_value, list) and isinstance(second_value, list):
        return right((first, second))


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


def find_match(input):  # returns index of matching bracket pair input must be valid parenthesis 
    count = 0
    for i,item in enumerate(input):
        if item == '[':
            count += 1
        elif item == ']':
            count -= 1
            if count == 0:
                return i


def format_input(input,output = None):  # use recursion
    #print(output)
    if output == None:
        output = []
    for i,char in enumerate(input):
        if char == ',':
            continue
        elif char == '[':
            output.append(format_input(input[i+1:find_match(input[i:])],output = output))
        elif char.isdigit(): #else
            output.append(int(char))
    print(output)
    return list(output)
            


def main():  # use the thing from day 7
    text = read_file(get_input_file()).splitlines()
    f_text = []
    correct_count = 0
    for i, pair in enumerate(text, 1):
        print(pair, "\n")
        if right(pair):
            correct_count += i


if __name__ == "__main__":
    # print(main())
    print(format_input('[4,4],4,4'))
    pass
