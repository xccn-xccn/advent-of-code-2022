square = [[3, 0, 3, 7, 3],
[2, 5, 5, 1, 2],
[6, 5, 3, 3, 2],
[3, 3, 5, 4, 9],
[3, 5, 3, 9, 0]]
for y_index,line in enumerate(square[1:-1], 1):
    for x_index,tree in enumerate(line[1:-1], 1):
        print(x_index,y_index,tree)