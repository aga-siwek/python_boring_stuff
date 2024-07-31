


def print_board(the_board):
    print()
    print(the_board["Top_L"] + "|" + the_board["Top_M"] + "|" + the_board["Top_R"])
    print("-+-+-")
    print(the_board["Mid_L"] + "|" + the_board["Mid_M"] + "|" + the_board["Mid_R"])
    print("-+-+-")
    print(the_board["Low_L"] + "|" + the_board["Low_M"] + "|" + the_board["Low_R"])
    print()



def make_move(the_board, player):
    for keys in the_board.keys():
        if the_board[keys] == " ":
            print(keys)
    print()
    player_move = input(f"for {player}, choose available ones from place: ")
    the_board[player_move] = player
    print_board(the_board)
    
def compare_win_move_with_board(the_board, j, player):
    point = 0
    for k, v in the_board.items():
        if k == j and v == player:
            point += 1
            return True
    return False



def check_win(the_board, player):

    the_win_move = [["Top_L", "Top_M", "Top_R"],
                    ["Mid_L", "Mid_M", "Mid_R"],
                    ["Low_L", "Low_M", "Low_R"],
                    ["Top_L", "Mid_M", "Low_R"],
                    ["Top_R", "Mid_M", "Low_L"],
                    ["Top_L", "Mid_L", "Tow_L"],
                    ["Top_M", "Mid_M", "Low_M"],
                    ["Top_R", "Mid_R", "Low_R"]]


    # check the list,
    for index, item in enumerate(the_win_move):
        win_point = 0
        #check the position in the list 
        for j in item:
            #open game board and compare with the win list 
            if compare_win_move_with_board(the_board, j, player):
                win_point += 1

          
            # print(a)
            # if compare_win_move_with_board(the_board, j, player):

            #     return True
            # for k, v in the_board.items():
            #     if k == j and v == player:
            #         win_point += 1
        print(win_point)
        if win_point == 3:
            return True
    return False


def tic_tac_toe_game():
    the_board = {"Top_L": " ", "Top_M":" ", "Top_R":" ",
                 "Mid_L": " ", "Mid_M":" ", "Mid_R":" ",
                 "Low_L": " ", "Low_M":" ", "Low_R":" "}
    max_turns = 9
    turn = 0
    current_player = "X"
    
    print_board(the_board)
    while turn < max_turns:
        
        make_move(the_board, current_player)
        if check_win(the_board, current_player):
            print (f"{current_player} player won")
            return True
        
        turn += 1

        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"

        
        # make_move(the_board, "0")
        # turn += 1 
        # if check_win(the_board, "0"):
        #     print ("0 player won")
        #     return

    print("draw")




tic_tac_toe_game()



