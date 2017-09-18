import numpy

np = numpy


# calculates the forward probabilities, to be partnered with backward to be used in the welch-baum algorithm
# the forward algorithm uses the same tactics as the viterbi algorithm but sums past states instead of maximizing them
# m loop inputs all values for the first time course to give a baseline for the recursive algorithm
# i loop keeps track of what time course you are calculating for
# k loop keeps track of what state you are in
# n loop goes back to previous time course to add on to the last probability
# t loop calculates the end value

def forward(state_probs, emission_probs, steps, emissions, non_silent_states, states):
    matrix = np.zeros((len(state_probs) / 2, steps + 1))
    matrix[0][0] = 1
    for m in range(1, len(states) + 1):
        if m in non_silent_states:
            matrix[m][1] = state_probs["0" + str(m)] * emission_probs[str(m) + emissions[0]]
        else:
            matrix[m][1] = state_probs["0" + str(m)]
    for i in range(2, steps + 1):
        for k in range(1, len(states)+1):
            total = 0
            if k in non_silent_states:
                for n in range(1, len(states) + 1):
                    total += matrix[n][i-1] * state_probs[str(n)+str(k)] * emission_probs[str(k)+emissions[i-1]]
            else:
                for n in range(1, len(states) + 1):
                    total += matrix[i-1][n] * state_probs[str(n) + str(k)]
            matrix[k][i] = total
        if i == 4:
            total = 0
            for t in range(1, len(states)+1):
                total += matrix[t][i] * state_probs[str(t)+"3"]
            matrix[t+1][i] = total
    print(matrix)

# number of time courses measured
steps = 4

# list of states
states = [1, 2]

# list of states that can emit an output(in this case X or Y)
non_silent_states = [1, 2]

# dict of probabilities to switch between states (ex: 12 is the probability to move from state 1 to 2
state_probs = {"01": 1, "02": 0, "11": 0.125, "12": 0.75, "13": 0.125, "22": 0.25, "21": 0.5, "23": 0.25}

# dict of probabilities to emit from a non silent state (ex: 1X is the probability to emit X from state 1)
emission_probs = {"1X": 0.875, "1Y": 0.125, "2X": 0.0625, "2Y": 0.9375}

# list of emissions measured during the time frame
emissions = ["X", "X", "X", "X"]

forward(state_probs, emission_probs, steps, emissions, non_silent_states, states)
