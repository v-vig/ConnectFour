# sample input
# .ryyrry,.rryry.,..y.r..,..y....,.......,....... red A 4

config = input()
initial_state = config.split(" ")[0] # separate initial state
initial_state = initial_state.split(",") # separate initial state into rows

state = []
for x in initial_state:
    state.append(list(x))

is_red_next = False
if (config.split(" ")[1] == "red"):
    is_red_next = True

alpha_beta_ON = False
if (config.split(" ")[2] == "A"):
    alpha_beta_ON = True

max_depth = config.split(" ")[3]


def score(state, player):
    "This prints a passed string into this function"
