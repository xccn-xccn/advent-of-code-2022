from sys import argv

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


def main():
    text = list(map(list,read_file(get_input_file()).splitlines()))
    for line in text:
        print(line)

    queue = [[(0,0),0]]
    visited = set((0,0))



    while queue:
        current_node = queue.pop()
        y,x = current_node[0]
        move_count = current_node[1]+1
        for neighbor in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            neighbour_y,neighbor_x = neighbor
            print(neighbour,neighbor_x,neighbour_y)
            if 0 <= neighbour_y < len(text) and 0 <= neighbour_x < len(text[0]) and neighbor not in visited and ord(text[y][x])+1 >= ord:
                queue.insert(-binary_search([x[1] for x in possible],move_count),[neighbour,move_count])
                visited.add(neighbor)

if __name__ == "__main__":
    print(main())
