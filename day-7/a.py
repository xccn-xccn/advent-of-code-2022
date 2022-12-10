import re
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text

def get_nested(index,f_list):
  temp_list = f_list
  for i in index:
    print(i,'i is')
    temp_list = temp_list[i]
  return temp_list

def main():
  final = 0
  storage = []
  text = read_file("sample.txt").splitlines()
  index = []
  # print(text)
  for z,l in enumerate(text):
    # print('success',z)
    if l[2:4] == 'cd':
      if l[-1] == '/':
        index.clear()
      elif l[-1] == '.':
        index.pop()
      elif l[5].isalpha(): 
        c_dir = get_nested(index,storage)
        index.append(len(c_dir))
        c_dir.append([])
      
    elif l[0].isdigit():
      c_dir = get_nested(index,storage)
      c_dir.append(int(re.search('[0-9]+',l).group()))
  index.clear()
  
  files = []
  for item in storage:
    if not isinstance(item,list):
      files.append(item)
  storage = list(filter(lambda x: isinstance(x,list),storage))
  print(storage)
  while True:
    print('a',index)
    c_dir = get_nested(index,storage)
    for i,item in enumerate(c_dir):
      if isinstance(item,list):
        index.append(i)
        break
      if i == len(c_dir)-1:
        if sum(c_dir) < 100_000:
          
          final += sum(c_dir)
        if index == []:
          return final
        sum_list = sum(c_dir)
        c_dir.clear()
        c_dir = get_nested(index[:-1],storage)
        # print('\n about to remove any empty lists', c_dir,index,index[-1])
        c_dir[index[-1]] = sum_list
        # print(c_dir)
        
        # c_dir = sum(c_dir) #change
        
        index.pop()
        
  return final
if __name__ == "__main__":
    print(main())

#128965 1141028