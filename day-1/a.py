def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
    text = read_file("input.txt").split("\n\n")
    for i,e in enumerate(text):
        text[i] = sum(int(x) for x in e.splitlines())
    print(max(text))


if __name__ == "__main__":
    main()