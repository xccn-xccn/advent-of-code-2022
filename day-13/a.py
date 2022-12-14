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


def main(): #use the thing from day 7
    text = read_file(get_input_file()).split('\n\n')
    for pair in text:
        print(pair,'\n')

if __name__ == "__main__":
    print(main())