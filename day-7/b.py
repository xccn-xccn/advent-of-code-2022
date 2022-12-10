import re
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text

def get_nested(index,f_list):
  temp_list = f_list
  for i in index:
    temp_list = temp_list[i]
  return temp_list

def find(storage):
  index = []
  files = []
  for item in storage:
    if not isinstance(item,list):
      files.append(item)
  files = sum(files)
  storage = list(filter(lambda x: isinstance(x,list),storage))
  while True:
    # print(files,'files')
    c_dir = get_nested(index,storage)
    for i,item in enumerate(c_dir):
      if isinstance(item,list):
        index.append(i)
        break
      if i == len(c_dir)-1:
        # print(storage,'\n',index)
        if index == []:
          # print(storage,type(storage))
          # print(sum(storage))
          files += sum(storage)
          return storage,files
        
        sum_list = sum(c_dir)
        if len(index) != 1:
          storage.append(sum_list)
        c_dir.clear()
        c_dir = get_nested(index[:-1],storage)
        c_dir[index[-1]] = sum_list
        
        
        index.pop()
 
def get_sizes(storage, result): #remember
  total = 0
  for item in storage:
    if isinstance(item, int):
      total += item
    else:
      total += get_sizes(item, result)
  result.append(total)
  return total

def get_sizes2(storage):
  total = 0
  result = []
  for item in storage:
    if isinstance(item, int):
      total += item
    else:
      sub_sizes = get_sizes2(item)
      total += sub_sizes[-1]
      result.extend(sub_sizes)
  result.append(total)
  return result

def get_sizes3(storage, result):
  if isinstance(storage, int):
    return storage
  total = 0
  for item in storage:
    total += get_sizes3(item, result)
  result.append(total)
  return total

def get_sizes4(storage, result):
  if isinstance(storage, int):
    return storage
  result.append(sum(get_sizes4(item, result) for item in storage))
  return result[-1]

def main():
  final = 0
  storage = []
  text = read_file("input.txt").splitlines()
  index = []
  # # print(text)
  for z,l in enumerate(text):
    # # print('success',z)
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
  result = []
  # storage,need = find(storage)
  need = get_sizes(storage, result)
  storage = sorted(result)

  need = 30_000_000 - (70_000_000 - need)
  # print(need,storage)
  for dir in storage:
    if dir > need:
      return dir
if __name__ == "__main__":
    print(main())

#128965 1141028