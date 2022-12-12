from sys import argv
from collections import deque
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"

        
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


def valid(grid,y,x,visited,special,current_letter): 
    
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y,x) not in visited):
        return False
    new_letter = grid[y][x]    
    return ord(special.get(current_letter,current_letter))+1 >= ord(special.get(new_letter,new_letter))
    

def main():
    grid = list(map(list,read_file(get_input_file()).splitlines()))
    special = {"S":"a","E":"z"}
    for y,line in enumerate(grid):
        for x,square in enumerate(line):
            if square == 'S':
                start = (y,x)

    paths = deque([[[start]]])
    visited = set((0,0))



    while True:
        
        current_node = paths.popleft()
        currently_taken = current_node[0]
        current_y,current_x = currently_taken[-1]
        current_letter = grid[current_y][current_x]
        for neighbour in [(current_y - 1, current_x), (current_y + 1, current_x), (current_y, current_x - 1), (current_y, current_x + 1)]:
            neighbour_y,neighbour_x = neighbour
            if valid(grid,neighbour_y,neighbour_x,visited,special,current_letter):
                temp_path = currently_taken.copy()
                temp_path.append((neighbour_y,neighbour_x))
                paths.append([temp_path])
                visited.add(neighbour)
                if grid[neighbour_y][neighbour_x] == "E":
                    return len(temp_path)-1
if __name__ == "__main__":
    print(main())
