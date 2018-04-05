# sample input
# .ryyrry,.rryry.,..y.r..,..y....,.......,....... red A 4

# assume player is in the form "r" or "y"
# as the board is presented UPSIDE DOWN
import sys

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

                    # check top right
                    if (y-1 < 0 or x+1 < board_width-1 and state[y-1][x+1] != player):
                        counter = 1
                        while (True):
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

                    # check bottom left
                    if (y-1 < 0 or x - 1 >= 0 and state[y-1][x-1]!= player):
                        counter = 1
                        while (True):
                            if (x+counter <= board_width-1 and y+counter <= board_height-1 and state[y+counter][x+counter] == player):
                                counter +=1
                            else:
                                if (counter == 2 ):
                                    double +=1
                                if (counter == 3):
                                    triple +=1
                                if (counter == 4):
                                    quadruple +=1
                                break

                # check left
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

def evaluation(state):
    return score(state, "r") - score(state, "y")

board_height = 6
board_width = 7

initial_state = sys.argv[1] # separate initial state
initial_state = initial_state.split(",") # separate initial state into rows
print(initial_state)
state = []
for x in initial_state:
    state.append(list(x))
is_red_next = False
if (sys.argv[2] == "red"):
    is_red_next = True
alpha_beta_ON = False
if (sys.argv[3] == "A"):
    alpha_beta_ON = True
max_depth = sys.argv[4]

# generate a game state tree of depth max_depth

# perform minimax algorithm on the tree
# return winning child
class Node:
    def _init_(self, score, state, player, children = None):
        self.score = score(state, player)
        self.children = children or []
        self.parent = None

    def generate_children(self, state):
        for x in range(board_width):
            def child(score, state, player):
