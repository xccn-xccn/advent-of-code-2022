import re
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def main():
  count = 0 
  text = read_file("input.txt").splitlines()
  for l in text:
    first_l,first_u,second_l,second_u = list(map(int,re.findall(r"\d+",l)))
    if (second_l >= first_l and second_u <= first_u) or (first_l >= second_l and first_u <= second_u):
      count += 1
  return count
  
if __name__ == "__main__":
    print(main())