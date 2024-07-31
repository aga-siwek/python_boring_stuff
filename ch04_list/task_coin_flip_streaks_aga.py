NUMBER_OF_THROWS = 6
NUMBER_OF_TRIES = 10000
THE_SAME_COINS_REQUESTED = 6





def throws_a_coin():
    import random
    coin_flip_game = []
    # for experiment in range(NUMBER_OF_TRIES):
    for x in range(NUMBER_OF_THROWS):
        coin = random.randint(0,1)
        if coin == 0:
            coin = "T"
            coin_flip_game.append(coin)
        if coin == 1:
            coin = "H"
            coin_flip_game.append(coin)
    return coin_flip_game




def check_a_coin_neighbors(coin_flip_game, THE_SAME_COINS_REQUESTED):
    tails_result = 0
    head_result = 0

    for index, item in enumerate(coin_flip_game):
        the_same_coins = 0
        if item == "T":
            for i in range(THE_SAME_COINS_REQUESTED):
                index_to_check = index + i
                if index_to_check <= len(coin_flip_game)-1:
                    if coin_flip_game[index_to_check] == "T":
                        the_same_coins += 1
            if the_same_coins == THE_SAME_COINS_REQUESTED:
                tails_result += 1

      
        elif item == "H":
            for i in range(THE_SAME_COINS_REQUESTED):
                index_to_check = index + i
                if index_to_check <= len(coin_flip_game)-1:
                    if coin_flip_game[index_to_check] == "H":
                        the_same_coins += 1

            if the_same_coins == THE_SAME_COINS_REQUESTED:
                head_result += 1
    # print("t= " + str(tails_result))
    # print("h= "+ str(head_result))



    if tails_result > 0 or head_result > 0:
        return 1
    else:
        return 0


score = 0
for x in range(NUMBER_OF_TRIES):
    
    coin_flip_game = throws_a_coin()
    result = check_a_coin_neighbors(coin_flip_game, THE_SAME_COINS_REQUESTED)
    score = score + result
    # print("result" + str(result))
    # print("score" + str(score))
    # print(coin_flip_game)
    # print()


print(str(THE_SAME_COINS_REQUESTED) + " same neighbors, in the " + str(NUMBER_OF_THROWS) + " throws. The result is: " + str(score) + " for " + str(NUMBER_OF_TRIES) + " tries.")