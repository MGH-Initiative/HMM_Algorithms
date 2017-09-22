import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

init_states = {"B", "1", "2","E"}
states = {"1", "2"}

current_state = "B"

start_prob = 1

emissions = {"x", 'y'}

# dictionaries with transitory probabilities ( the variable name is the starting location and the key is the end)
#   ex: dictionary named "one" holds keys to all the transition probabilities of going from other states TO one

b = {"B": 0, "1": 1, "2":0, "E":0}
one = {"B": 0, "1": 1 / 8, "2": 3 / 4, "E": 1 / 8}
two = {"B": 0, "1": 3/4, "2": 1/4,"E": 0}
e = {"B": 0, "1": 1/8, "2": 1/4, "E": 0}

allStates = [b, one, two, e]  # a vector of dictionaries

# dictionary with the respective probabilities for emitted states x and y

x = {"1": 7 / 8, "2": 1 / 16}

y = {"1": 1 / 8, "2": 15 / 16}


#####################################################

# function that specifies all the base cases

def hmm_v(state, time):  # state is char and time is int

    # three dimensional matrix that represents the table provided in the paper


    matrix = np.zeros((len(emissions), len(init_states), time + 1))

    # only possible state in time course 0 is B

    matrix[:, 0, 0] = start_prob

    # temporary array that holds the transitory probabilities


    for i in range(1, time + 1):
        for st in states:
            for j in range(len(emissions)):

                temp = []
                transit_prob = max(matrix[j, :, i-1])
                temp.append(transit_prob)










    return matrix

print(hmm_v("B", 4))
