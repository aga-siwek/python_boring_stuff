the_board = {"Top_L": " ", "Top_M":" ", "Top_R":" ",
             "Mid_L": " ", "Mid_M":" ", "Mid_R":" ",
             "Low_L": " ", "Low_M":" ", "Low_R":" "}

turn = "X"

def print_board(the_board):
    

    print(the_board["Top_L"] + "|" + the_board["Top_M"] + "|" + the_board["Top_R"])
    print("-+-+-")
    print(the_board["Mid_L"] + "|" + the_board["Mid_M"] + "|" + the_board["Mid_R"])
    print("-+-+-")
    print(the_board["Low_L"] + "|" + the_board["Low_M"] + "|" + the_board["Low_R"])
    print()

for i in range(9):
    print_board(the_board)
    print(f"Turn for {turn}. Move on which space?")
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "0"
    else:
        turn = "X"
print_board(the_board)