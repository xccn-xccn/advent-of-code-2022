def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
    points = 0
    win = {1:2, 2:3, 3:1}
    lose = {2:1, 3:2, 1:3}
    gain = {"X":1,"Y":2,"Z":3}
    text = read_file("day-2/input.txt")
    for l in text.splitlines():
        op,me = ord(l[:1])-64, l[2:]
        if me == "Z":
            points += 6 + win[op]
        elif me == "Y":
            points += 3 + op
        else:
            points += lose[op]
    print(points)



if __name__ == "__main__":
    main()