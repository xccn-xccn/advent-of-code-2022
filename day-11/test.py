#print(int("".join('- 1'.split())))
# import re
# print(re.findall('[\+*]', '3 + 4 + 7 * 3'))
# operator = re.search('[\+*]', ' Operation: new = old * 19').group(0)
alist = [[1,2,3], [4,5,6], [7,8,9]]
for array in alist:
    array.append(10)
print(array, alist)