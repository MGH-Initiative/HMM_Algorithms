import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

init_states = ["B", "1", "2","E"]
states = ["1", "2","E"]
num_states = 4
current_state = "B"

start_prob = 1

time_course = 4
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

emissionCourse = [x,x,x]

num_emissions = 2
#####################################################

# function that specifies all the base cases

def hmm_vit(state, time):  # state is char and time is int

    # three dimensional matrix that represents the table provided in the paper

    matrix = np.zeros((len(init_states), time_course + 1))

    # only possible state in time course 0 is B

    matrix[0, 0] = start_prob

    for i in range(1, time_course + 1):
        for currst in states:
            current_state = currst
            temp = []
            for prevst in range(num_states): #cycles thru all the states of the prev time course
                prevStateDictionary = allStates[prevst]
                trans_prob = prevStateDictionary[current_state] #finds trans probability from prev state to current state
                if currst!="E":
                    currEmissions = emissionCourse[i-1]
                    stateEmit = currEmissions[current_state]
                    temp.append(trans_prob*stateEmit*matrix[prevst,i-1])
                else:
                    temp.append(trans_prob*matrix[prevst,i-1])
            max_prob = max(temp)
            matrix[init_states.index(current_state), i] = max_prob


    return matrix[init_states.index(state),time]

print(hmm_vit("1", 4))
