from sys import argv
from functools import reduce

def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"

def indexing(square,x,y,iteration):
    #print(x,y,'x,y')
    if iteration == 0:
        return square[y][:x][::-1]
    elif iteration == 1:
        return square[y][x+1:]
    elif iteration == 2:
        return [line[x] for line in square[:y]][::-1]
    else:
        return [line[x] for line in square[y+1:]]

def possible_seeable(square,x_index,y_index):
    possible = []
    for iteration in range(4):
        possible.append(indexing(square,x_index,y_index,iteration))
    return possible

def seeable(tree,others):
    seen_trees = []
    for other_trees in others:
        for i,other_tree in enumerate(other_trees):
            if other_tree >= tree or i == len(other_trees)-1:
                seen_trees.append(i+1)
                break
    return seen_trees
def can_see_line(line):
    seen = set()
    for iteration in range(2):
        tallest = -1
        for x_index, tree in enumerate(line):
            if tree > tallest:
                seen.add(x_index if iteration == 0 else len(line) - x_index - 1)
                tallest = tree
        line.reverse()
    return seen


def main():
    highest = 1
    square = [list(map(int, line)) for line in read_file(get_input_file()).splitlines()]
    for y_index,line in enumerate(square[1:-1], 1):
        for x_index,tree in enumerate(line[1:-1], 1):
            current_score = 1
            #print(x_index,y_index)
            possible = possible_seeable(square,x_index,y_index)
            #current_score = reduce(lambda a,b: a*b,seeable(tree,possible))
            #print(possible,'possible',tree)
            seeable_count = seeable(tree,possible)
            #print(seeable_count,'seeable count')
            for score in seeable_count:
                current_score *= score
                #print(current_score)

            #print(current_score)
            if current_score > highest:
                highest = current_score
                #print('new highest score', highest)
    return highest

if __name__ == "__main__":
    print(main())
