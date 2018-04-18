board_height = 6
board_width = 7

# note 2d arrays are indexed as [Y-index][X-index]
def score(state, player):
    single, double, triple, quadruple, total = (0, 0, 0, 0, 0)
    for y in range(len(state)):
        for x in range(len(state[y])):
            if (state[y][x] == player):
                single+=1
                # check bottom
                if (y-1 < 0 or state[y-1][x] != player):
                    counter = 1

                    # see how far connection goes UPWARDS
                    while (True):
                        if (y+counter <= board_height-1 and state[y+counter][x] == player):
                            counter += 1
                        else:
                            if (counter == 2 ):
                                double +=1
                            if (counter == 3):
                                triple +=1
                            if (counter == 4):
                                quadruple +=1
                            break

                # see how far connection goes UPWARDS to the LEFT
                if (y-1 < 0 or x+1 > board_width-1 or state[y-1][x+1] != player):
                    counter = 1
                    while (True):
                        # print("CHECKING (" + str(x-counter)+ ", " + str(y + counter) + ")")
                        if (x-counter >= 0 and y+counter <= board_height-1 and state[y+counter][x-counter] == player):
                            counter += 1
                        else:
                            if (counter == 2 ):
                                double +=1
                            if (counter == 3):
                                triple +=1
                            if (counter == 4):
                                quadruple +=1
                            break

                # see how far connection goes UPWARDS to the RIGHT
                if (y-1 < 0 or x-1 < 0 or state[y-1][x-1]!= player):
                    counter = 1
                    while (True):
                        if (x+counter <= board_width-1 and y+counter <= board_height-1 and state[y+counter][x+counter] == player):
                            counter +=1
                            # print("TOP RIGHT")
                        else:
                            if (counter == 2 ):
                                double +=1
                            if (counter == 3):
                                triple +=1
                            if (counter == 4):
                                quadruple +=1
                            break

                # check how far connection goes to the RIGHT
                if (x - 1 < 0 or state[y][x-1] != player):
                    counter = 1
                    while (True):
                        if (x+counter <= board_width-1 and state[y][x+counter] == player):
                            counter +=1
                        else:
                            if (counter == 2 ):
                                double +=1
                            if (counter == 3):
                                triple +=1
                            if (counter == 4):
                                quadruple +=1
                            break

    total = single + 10*double + 100*triple + 1000*quadruple
    return total
