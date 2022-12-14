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


def right(pair):
    first,second = pair
    if isinstance(first,int) and isinstance(second,int):
        if first == second:
            return right(pair[1:])
    elif isinstance(first,list) and isinstance(second,list):
        return right((first,second))
    
def main(): #use the thing from day 7
    text = read_file(get_input_file()).split('\n\n')
    correct_count = 0
    for pair in text:
        print(pair,'\n')
        if right(pair):
            correct_count += 1

if __name__ == "__main__":
    print(main())