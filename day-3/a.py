def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text

def main():
  points = 0
  text = read_file("input.txt")
  for l in text.splitlines():
    first,last = l[:len(l)//2],l[len(l)//2:]
    for c in first:
      if c in last:
        if ord(c) > 96:
          points += ord(c) - 96 
        else:
          points += ord(c) - 38
        break
        
  return points
if __name__ == "__main__":
    print(main())
