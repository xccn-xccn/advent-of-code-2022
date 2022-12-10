def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text

def main():
  text = read_file("input.txt")
  for i in range(0,len(text)-14):
    chars = text[i:i+14]
    if len(set(chars)) == 14:
      return i + 14

if __name__ == "__main__":
    print(main())