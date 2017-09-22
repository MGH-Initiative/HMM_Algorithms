import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

states = {"B", "1", "2", "E"}

emissions = {"x", 'y'}

# dictionary with all transitory probabilities

a = {"B1": 1, "B2": 0, "BE": 0, "11": 1 / 8, "12": 3 / 4, "1E": 1 / 8, "21": 1 / 2, "22": 1 / 4, "2E": 1 / 4}

# dictionary with the respective probabilities for emitted states x and y

x = {"1": 7 / 8, "2": 1 / 16}

y = {"1": 1 / 8, "2": 15 / 16}

# function that specifies all the base cases

def hmm_v(state, time):

    # three dimensional matrix that represents the table provided in the paper

    matrix = np.zeros((len(emissions), len(states), time + 1))

    for i in range(time):



print(hmm_v("B", 4))
