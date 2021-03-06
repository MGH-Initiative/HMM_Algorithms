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
    for i in reversed(range(1, dimx - 1)):
        if i in non_silent_states:
            matrix[i, dimy - 1] = state_probs["3" + str(i)]
        else:
            matrix[i, dimy - 1] = state_probs["3" + str(i)]
    for r in range(1, dimy - 2):
        for c in reversed(range(0, dimx)):
            tot = 0
            if r in non_silent_states:
                for s in range(1, len(states) + 1):
                    tot += matrix[s, c + 1] * state_probs[str(r) + str(s)] * emission_probs[str(s) + emissions[c]]
            """else:
                for s in reversed(range(1, len(states) + 1)):
                    tot += matrix[s, c + 1] * state_probs[str(s) + str(c)]"""
            matrix[r][c] = tot

    tot = 0
    for s in range(1, len(states) + 1):
        tot += matrix[s, 1] * state_probs[str(0) + str(s)] * emission_probs[str(s) + emissions[0]]
        print(tot)
    matrix[0, 0] = tot
    return matrix


# number of time courses measured
sp = 4

# list of states
st = [1, 2]

# list of states that can emit an output(in this case X or Y)
nss = [1, 2]

# dict of probabilities to switch between states (ex: 12 is the probability to move from state 1 to 2
stp = {"31": 0.125, "32": 0.25, "11": 0.125, "12": 0.75, "22": 0.25, "21": 0.5, "01": 1, "02": 0}

# dict of probabilities to emit from a non silent state (ex: 1X is the probability to emit X from state 1)
ep = {"0X": 0, "1X": 0.875, "1Y": 0.125, "2X": 0.0625, "2Y": 0.9375}

# list of emissions measured during the time frame
e = ["X", "X", "X", "X"]

setup(sp, st, nss, e, stp, ep)

print(backward())
print(197/(2**14), 15/(2**8))
