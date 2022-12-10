def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text

def main():
  points = 0
  text = read_file("input.txt").splitlines()
  for l in range(0,len(text),3):
    first,second,third = text[l],text[l+1],text[l+2]
    for c in first:
      if c in second and c in third:
        if ord(c) > 96:
          points += ord(c) - 96 
        else:
          points += ord(c) - 38
        break
        print(points)
  return points
if __name__ == "__main__":
    print(main())
