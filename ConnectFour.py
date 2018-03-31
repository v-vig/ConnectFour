config = input() # read game config from stdin
initial_state = config.split(" ")[0] # separate initial state
initial_state = initial_state.split(",") # separate initial state into rows

state = []
for x in initial_state:
    state.append(list(x))
