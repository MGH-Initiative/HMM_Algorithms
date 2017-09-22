import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

states = {"B", "1", "2", "E"}

start_state = "B"

emissions = {"x", 'y'}

# dictionaries with transitory probabilities ( the title is the destination and the key is the starting location)
#   ex: dictionary named "one" holds keys to all the transition probabilities of going from other states TO one

b = {"B":0, "1":0, "2":0, "E":0}
one = {"B":1, "1":1/8, "2":1/2, "E":0}
two = {"B":0, "1":3/4, "2":1/4,"E":0}
e = {"B":0, "1":1/8, "2":1/4, "E":0}
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

    for i in range(1, time + 1):
        #for st in range(0, len(states)):
         # matrix[1,st,i] =
         # lulu in progress code:
         # the idea is that for every current state in a time course:
         # you go through all the previous states of the last time course
         # and multiply by their transitions to the current state
         # then take the max of these values for the one matrix[x,y,z] value
        for value in all.items():
            print(value)








print(hmm_v("B", 4))
