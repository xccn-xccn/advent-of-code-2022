import copy
def shortest_path(topology, start, end):
    possible = [[[start],0]]
    finished = []
    lowest = 999999999999999999999
    flag = False
    while possible:
        current = possible.pop()
        for node,time in topology[current[0][-1]].items():
            if node in current[0]:
                continue
            temp = copy.deepcopy(current)
            temp[0].append(node)
            temp[1] += time
            if temp[1] > lowest:
                continue
            if node == end:
                if temp[1] < lowest:
                    finished = [temp[0]]
                    lowest = temp[1]
                elif temp[1] == lowest:
                    finished.append(temp[0])
                continue
            possible.insert(-binary_search([x[1] for x in possible],temp[1]),temp)
            
            
    a = min([len(x) for x in finished])
    for i,s in enumerate(finished):
        if len(s) > a:
            finished.pop(i)
    return finished

def binary_search(arr, x):
    low,high,mid = 0,len(arr) - 1,0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low