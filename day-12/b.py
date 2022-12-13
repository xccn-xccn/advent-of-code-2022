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


def set_variables():
    current_node = paths.popleft()
    currently_taken = current_node[0]
    current_y,current_x = currently_taken[-1]
    current_letter = grid[current_y][current_x]
    return current_node,currently_taken,current_y,current_x,current_letter


def find_start(seen):
    for y,line in enumerate(grid):
        for x,square in enumerate(line):
            if (square == 'S' or square == 'a') and (y,x) not in seen:
                return y,x
def valid(y,x,visited,special,current_letter): 
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y,x) not in visited):
        return False
    new_letter = grid[y][x]    
    return ord(special.get(current_letter,current_letter))+1 >= ord(special.get(new_letter,new_letter))
    

def main():
    global grid,paths,special,visited
    grid = list(map(list,read_file(get_input_file()).splitlines()))
    special = {"S":"a","E":"z"}
    best_path = 999
    seen_start = set()
    while True:
        #print(best_path)
        start = find_start(seen_start)
        if start == None:
            return best_path
        seen_start.add(start)
        #print(start)
        paths = deque([[[start]]])
        visited = set(start)
        end = False
        while not end:
            #print(paths)
            current_node,currently_taken,current_y,current_x,current_letter = set_variables()
            for neighbour in [(current_y - 1, current_x), (current_y + 1, current_x), (current_y, current_x - 1), (current_y, current_x + 1)]:
                neighbour_y,neighbour_x = neighbour
                if valid(neighbour_y,neighbour_x,visited,special,current_letter):
                    temp_path = currently_taken.copy()
                    temp_path.append(neighbour)
                    paths.append([temp_path])
                    visited.add(neighbour)
                    if grid[neighbour_y][neighbour_x] == "E":
                        if len(temp_path)-1 < best_path:
                            best_path = len(temp_path) - 1
                        end = True
                        break
            if not paths:
                break
if __name__ == "__main__":
    print(main())
