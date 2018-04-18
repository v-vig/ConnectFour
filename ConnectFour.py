# sample input
# .ryyrry,.rryry.,..y.r..,..y....,.......,....... red A 4

# assume player is in the form "r" or "y"
# as the board is presented UPSIDE DOWN
import sys
from score import score

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

print("Score = " + str(score(state,"y")))
