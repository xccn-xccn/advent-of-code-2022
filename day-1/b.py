def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
    text = read_file("input.txt").split("\n\n")
    for i,e in enumerate(text):
        text[i] = sum(int(x) for x in e.splitlines())
    print(sorted(text)[-3:])
    return sum(sorted(text)[-3:])
    



if __name__ == "__main__":
    print(main())