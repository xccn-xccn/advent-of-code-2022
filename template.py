def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
    text = read_file("sample.txt")


if __name__ == "__main__":
    main()