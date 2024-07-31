import random, copy, time
board = []

# const variables should be UPPERCASE
WIDTH = 16
HEIGHT = 16
LIFE_CELLS = 42
DELAY_BETWEEN_STEPS = 1

DEAD_CELL = " "
LIVE_CELL = "#"


for i in range(HEIGHT):
    board.append([DEAD_CELL] * WIDTH)


# you can random same position twice
# for i in range(LIFE_CELLS):
#     board[random.randint(0,(HEIGHT-1))][random.randint(0, (WIDTH-1))] = "#"

number_of_try = 0
while number_of_try <= LIFE_CELLS:

    y = random.randint(0,(HEIGHT-1))
    x = random.randint(0, (WIDTH-1))
    if board[y][x] == DEAD_CELL:
        board[y][x] = LIVE_CELL
        number_of_try += 1






def print_board(board):
    for index, item in enumerate(board):
        print(item)
    print("")

def get_number_of_neighbours(board, x, y):
    number_of_neighbours = 0

    if board[(y-1)%HEIGHT][(x-1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1
    if board[(y-1)%HEIGHT][x] == LIVE_CELL:
        number_of_neighbours += 1
    if board[(y-1)%HEIGHT][(x+1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1
    if board[y][(x-1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1
    if board[y][(x+1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1
    if board[(y+1)%HEIGHT][(x-1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1
    if board[(y+1)%HEIGHT][x] == LIVE_CELL:
        number_of_neighbours += 1
    if board[(y+1)%HEIGHT][(x+1)%WIDTH] == LIVE_CELL:
        number_of_neighbours += 1

    return number_of_neighbours

def evaluate_next_step(board):
    previous_board = copy.deepcopy(board)

    for y in range (HEIGHT):
        for x in range (WIDTH):
            number_of_neighbours = get_number_of_neighbours(previous_board, x, y)
            
            if previous_board[y][x] == LIVE_CELL:
                if number_of_neighbours == 2 or number_of_neighbours == 3:
                    board[y][x] = LIVE_CELL
                else:
                    board[y][x] = DEAD_CELL
            else:
                if number_of_neighbours == 3:
                    board[y][x] = LIVE_CELL  

while True:
    time.sleep(DELAY_BETWEEN_STEPS)
    print_board(board)
    evaluate_next_step(board)


    # for index, item in enumerate(board):
    #     print(item)
    # print(" ")

    # previous_board = copy.deepcopy(board)

    # for y in range (HEIGHT):
    #     for x in range (WIDTH):
    #         # number_of_neighbours = get_number_of_neighbours(previous_board, x, y)
    #         point = 0
    #         if previous_board[(y-1)%HEIGHT][(x-1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[(y-1)%HEIGHT][x] == "#":
    #             point += 1
    #         if previous_board[(y-1)%HEIGHT][(x+1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[y][(x-1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[y][(x+1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[(y+1)%HEIGHT][(x-1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[(y+1)%HEIGHT][x] == "#":
    #             point += 1
    #         if previous_board[(y+1)%HEIGHT][(x+1)%WIDTH] == "#":
    #             point += 1
    #         if previous_board[y][x] == "#":
    #             if point == 2 or point == 3:
    #                 board[y][x] = "#"
    #             else:
    #                 board[y][x] = " "
    #         else:
    #             if point == 3:
    #                 board[y][x] = "#"  