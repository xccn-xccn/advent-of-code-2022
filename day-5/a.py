import re
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
  boxes = [[] for x in range(9)]
  u_boxes,instructions = read_file("input.txt").split("\n\n")
  for l in u_boxes.splitlines()[:-1][::-1]:
    for i,char in enumerate(l):
      if i%4 == 1 and char != ' ':
        boxes[i//4].append(char)
  for ins in instructions.splitlines():
    v,s,e = [int(n)-1 for n in re.findall('[0-9]+',ins)]
    for i in range(v+1):
      boxes[e].append(boxes[s].pop())
  return ''.join([x[-1] for x in boxes])
if __name__ == "__main__":
    print(main())