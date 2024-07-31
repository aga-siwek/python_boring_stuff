import random, copy, time
# [#] life cell, [ ] dead cell,  
# [#] - 2# = #, [#] - 3# = #
#[ ] - 3# = [#]


board = []
high = 10
WIDTH = 6
point = 0
first_life_number = 30
x = WIDTH - WIDTH
y = high - high




for i in range(high):
    board.append([" "]*WIDTH)


for i in range(first_life_number):
    x = random.randint(0,(high-1))
    y = random.randint(0,(WIDTH-1))
    board[x][y] = "#"


x = 0
y = 0
previous_board = copy.deepcopy(board)


while True:
            
            time.sleep(0.3)
            


            try:
                while x < high and y < WIDTH:
                    point = 0

                    if board[x][y] == " ":
                        if board[x][y+1] == "#":
                            point += 1
                        if board[x][y-1] == "#":
                            point += 1
                        if board[x-1][y] == "#":
                            point += 1
                        if board[x-1][y-1] == "#":
                            point += 1
                        if board[x-1][y+1] == "#":
                            point += 1
                        if board[x+1][y] == "#":
                            point += 1
                        if board[x+1][y-1] == "#":
                            point += 1
                        if board[x+1][y+1] == "#":
                            point += 1
                        print(point)
                        if point == 3:
                            previous_board[x][y] = "#"
                        point = 0
                        if x < high:
                            x += 1
                        else:
                            y += 1
                            x = 0
                    elif board[x][y] == "#":
                        if board[x][y+1] == "#":
                            point += 1
                        if board[x][y-1] == "#":
                            point += 1
                        if board[x-1][y] == "#":
                            point += 1
                        if board[x-1][y-1] == "#":
                            point += 1
                        if board[x-1][y+1] == "#":
                            point += 1
                        if board[x+1][y] == "#":
                            point += 1
                        if board[x+1][y-1] == "#":
                            point += 1
                        if board[x+1][y+1] == "#":
                            point += 1
                        if point != 3 or point != 2:
                            previous_board[x][y] = " "
                        print(point)
                        point = 0
                        if x < high:
                            x += 1
                        else:
                            y += 1

                   
            except IndexError:
                False

            board = previous_board
            for index, item in enumerate(board):
                print((item))
            print(" ")
            

            

            

