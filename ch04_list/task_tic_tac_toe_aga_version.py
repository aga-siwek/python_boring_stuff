


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

def check_win(the_board, player):
    if the_board["Top_L"] == player and the_board["Top_M"] == player and the_board["Top_R"] == player:
        return True
    if the_board["Mid_L"] == player and the_board["Mid_M"] == player and the_board["Mid_R"] == player:
        return True
    if the_board["Low_L"] == player and the_board["Low_M"] == player and the_board["Low_R"] == player:
        return True
    if the_board["Top_L"] == player and the_board["Mid_M"] == player and the_board["Low_R"] == player:
        return True
    if the_board["Top_R"] == player and the_board["Mid_M"] == player and the_board["Low_L"] == player:
        return True
    if the_board["Top_L"] == player and the_board["Mid_L"] == player and the_board["Low_L"] == player:
        return True
    if the_board["Top_M"] == player and the_board["Mid_M"] == player and the_board["Low_M"] == player:
        return True
    if the_board["Top_R"] == player and the_board["Mid_R"] == player and the_board["Low_R"] == player:
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
            return
        
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



