import numpy

np = numpy

# initialized and defined set of all potential states

states = {"B", "1", "2", "E"}

time_course = 4

# dictionary with all transitory probabilities

a = {"B1": 1, "B2": 0, "BE": 0, "11": 1 / 8, "12": 3 / 4, "1E": 1 / 8, "21": 1 / 2, "22": 1 / 4, "2E": 1 / 4}

# initialized a set to conatain all of the time course probabilities

matrices = []

# initialized the matrix to store the final probabilities

book_keeping = np.matrix(np.arange(time_course * len(states)).reshape((time_course, len(states))))

# dictionary with the respective probabilities for emitted states x and y

x = {"1": 7 / 8, "2": 1 / 16}

y = {"1": 1 / 8, "2": 15 / 16}

# function that specifies all the base cases

def hmm_v(state, time):

    """create and append all of the matrices that will contain each probability for each time coures
        + a final matrix that will contain final / maximum probabilities"""

    for i in range(time + 1):
        matrices.append(np.matrix(np.arange(time * len(states)).reshape((time, len(states)))))
    return matrices


def hmm_r():
    return hmm_r()

print(hmm_v(3))

"""def HMM_Vsauce(time_course):
    prob1 = 1
    currState = "B"
    for i in range(time_course):
        if prob1 * a[currState + "1"] * x["1"] > prob1 * a[currState + "2"] * x["2"]:
            prob1 = prob1 * a[currState + "1"]
            currState = "1"
            prob1 = prob1 * x["1"]
            print(prob1, currState)
        else:
            prob1 = prob1 * a[currState + "2"]
            currState = "2"
            prob1 = prob1 * x["2"]
            print(prob1, currState)
    return prob1, currState
    """