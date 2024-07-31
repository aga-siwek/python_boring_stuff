grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "0", "0", ".", ".", "."],
    ["0", "0", "0", "0", ".", "."],
    ["0", "0", "0", "0", "0", "."],
    [".", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "."],
    ["0", "0", "0", "0", ".", "."],
    [".", "0", "0", ".", ".", "."],
    ["X", ".", ".", ".", ".", "."]
    ]
x = len(grid[0])
y = len(grid)
# new_grid = []
# new_list =[]
# for column in range(x):
#     for row in range(y):
#         element = grid[row][column]
#         new_list.append(element)
#     new_grid.append(new_list)
#     new_list =[]

for i in range(x):
    for j in range(y):
        print(grid[(y-1)-j][i], end="")
    print("")

for i in range(x):
    for j in reversed(range(y)):
        print(grid[j][i], end="")
    print("")


