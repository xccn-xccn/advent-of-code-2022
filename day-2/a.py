def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
    points = 0
    win = {1:2,2:3,3:1}
    text = read_file("day-2/input.txt")
    for l in text.splitlines():
        op,me = ord(l[:1])-64, ord(l[2:])-87
        if win[op] == me:
            points += 6
        elif me == op:
            points += 3
        points += me
    print(points)



if __name__ == "__main__":
    main()