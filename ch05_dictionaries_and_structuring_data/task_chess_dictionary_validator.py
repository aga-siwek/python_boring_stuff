chess_board = {"a8":" ","b8":" ","c8":" ","d8":" ","e8":" ","f8":" ","g8":" ","h8":" ",
               "a7":" ","b7":" ","c7":" ","d7":" ","e7":" ","f7":"bpaw","g7":" ","h7":" ",
               "a6":" ","b6":" ","c6":"wqueen","d6":" ","e6":" ","f6":" ","g6":" ","h6":" ",
               "a5":" ","b5":" ","c5":" ","d5":" ","e5":" ","f5":" ","g5":" ","h5":"bqueen",
               "a4":" ","b4":" ","c4":" ","d4":" ","e4":" ","f4":" ","g4":" ","h4":" ",
               "a3":" ","b3":" ","c3":" ","d3":" ","e3":"wking","f3":" ","g3":" ","h3":" ",
               "a2":" ","b2":" ","c2":" ","d2":" ","e2":" ","f2":" ","g2":"bbishop","h2":" ",
               "a1":" ","b1":" ","c1":" ","d1":" ","e1":" ","f1":" ","g1":" ","h1":"bking"}



#1 black king, 1 white king max 16 white, max 16 black max 8 pawns

def allowed_board_check (chess_board):
    allowed_board = ["a8","b8","c8","d8","e8","f8","g8","h8",
               "a7","b7","c7","d7","e7","f7","g7","h7",
               "a6","b6","c6","d6","e6","f6","g6","h6",
               "a5","b5","c5","d5","e5","f5","g5","h5",
               "a4","b4","c4","d4","e4","f4","g4","h4",
               "a3","b3","c3","d3","e3","f3","g3","h3",
               "a2","b2","c2","d2","e2","f2","g2","h2",
               "a1","b1","c1","d1","e1","f1","g1","h1"]

    
    good_letters = 0

    for index, item in enumerate(allowed_board):
        for move in chess_board.keys():
            if item == move:
                good_letters += 1

    if good_letters != 64:
        return False
    
    return True

def allowed_figure_number(chess_board, player):
    figure_number = 0

    for v in chess_board.values():
        if player in v:
            figure_number += 1

    if figure_number > 16:
        return False
    
    return True

    
def queen_check(chess_board, player):
    queen = 0

    for v in chess_board.values():
        if (player + "queen") in v:
            queen += 1

        if queen > 1:
            return False
        
    return True
    
def king_check(chess_board, player):
    king = 0

    for v in chess_board.values():
        if (player + "king") in v:
            king += 1

        if king > 1:
            return False
        
    return True

def paws_check(chess_board, player):
    paws = 0

    for v in chess_board.values():
        if (player + "paws") in v:
            paws += 1

        if paws > 8:
            return False
        
    return True

def rock_check(chess_board, player):
    rock = 0

    for v in chess_board.values():
        if (player + "rock") in v:
            rock += 1

        if rock > 2:
            return False
        
    return True

def bishop_check(chess_board, player):
    bishop = 0

    for v in chess_board.values():
        if (player + "bishop") in v:
            bishop += 1

        if bishop > 2:
            return False
        
    return True

def knight_check(chess_board, player):
    knight = 0

    for v in chess_board.values():
        if (player + "knight") in v:
            knight += 1

        if knight > 2:
            return False
        
    return True

def available_figure_list_check(chess_board):
    available_figure_list = ["wqueen", "wking", "wpaw", "wbishop", "wknight", "wrock","bqueen", "bking", "bpaw", "bbishop", "bknight", "brock"]
    figures_all = 0
    available_figures = 0

    for index, iteam in enumerate(available_figure_list):
        for v in chess_board.values():
            if v == iteam:
                available_figures += 1
    

    for v in chess_board.values():
        if v != " " :
            figures_all += 1
            
    if available_figures == figures_all:
        return True
    return False

    
    # black_figures = 0
    # white_figures = 0 

    # for figures in chess_board.values():
    #     if figures != " ":
    #         figures_all += 1
    #     if figures.startswith("w"):
    #         white_figures += 1
    #     if figures.startswith("b"):
    #         black_figures += 1
    # if (black_figures + white_figures) == figures_all:
    #     return True
    # return False



def allowed_figures(chess_board, player):
    if (queen_check(chess_board, player) and
        king_check(chess_board, player) and
        paws_check(chess_board, player) and 
        rock_check(chess_board, player) and
        bishop_check(chess_board, player) and
        knight_check(chess_board, player)):
       return True
    return False



def chess_game_check(chess_board, player):
    print(f"Allowed board check {player}")
    print(allowed_board_check (chess_board))
    print(f"Allowed figure number {player}")
    print(allowed_figure_number(chess_board, player))
    print(f"Available figure list check {player}")
    print(available_figure_list_check(chess_board))
    print(f"Allowed figures {player}")
    print(allowed_figures(chess_board, player))


            
chess_game_check(chess_board, "w")
chess_game_check(chess_board, "b")

