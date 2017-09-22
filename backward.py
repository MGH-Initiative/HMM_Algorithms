import numpy

np = numpy

#init ints
steps = 0
end_states = 2
#init lists
states = []
non_silent_states = []
emissions = []
#init dictionaries
state_probs = {}
emission_probs = {}

def setup(sp, st, nss, e, stp, ep):
    global steps, states, non_silent_states, emissions, state_probs, emission_probs
    steps = sp
    states = st
    non_silent_states = nss
    emissions = e
    state_probs = stp
    emission_probs = ep
    return "setup done."


def backward():
    dimx, dimy = len(states) + end_states, steps + 1
    dim = (dimx, dimy)
    matrix = np.zeros(dim)
    matrix[dimx - 1, dimy - 1] = 1
    for i in reversed(range(1, dimy)):


    return matrix


# number of time courses measured
sp = 4

# list of states
st = [1, 2]

# list of states that can emit an output(in this case X or Y)
nss = [1, 2]

# dict of probabilities to switch between states (ex: 12 is the probability to move from state 1 to 2
stp = {"01": 1, "02": 0, "11": 0.125, "12": 0.75, "13": 0.125, "22": 0.25, "21": 0.5, "23": 0.25}

# dict of probabilities to emit from a non silent state (ex: 1X is the probability to emit X from state 1)
ep = {"1X": 0.875, "1Y": 0.125, "2X": 0.0625, "2Y": 0.9375}

# list of emissions measured during the time frame
e = ["X", "X", "X", "X"]

setup(sp, st, nss, e, stp, ep)

print(backward())
