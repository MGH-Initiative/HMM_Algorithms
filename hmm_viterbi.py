import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

states = {"B", "1", "2", "E"}

start_state = "B"

emissions = {"x", 'y'}

# dictionaries with transitory probabilities ( the key is the destination and the title is the starting location)

b = {"1" : 1, "2" : 0, "E" : 0}
one = {"1" : 1/8, "2" : 3/4, "E": 1/8 }
two = {"1" : 1/2, "2" : 1/4, "E" : 1/4}

all = {"B" : b, "1" : one, "two" : two}

# dictionary with the respective probabilities for emitted states x and y

x = {"1": 7 / 8, "2": 1 / 16}

y = {"1": 1 / 8, "2": 15 / 16}

#####################################################

# function that specifies all the base cases

def hmm_v(state, time):

    # three dimensional matrix that represents the table provided in the paper

    matrix = np.zeros((len(emissions), len(states), time + 1))

    matrix[:, 0, 0 ] = 1

    for i in range(0, time + 1):
        for value in all.items():
            print(value)








print(hmm_v("B", 4))
