import numpy

np = numpy

states = {"B", "1", "2", "E"}

a = {"B1": 1, "B2": 0, "BE": 0, "11": 1 / 8, "12": 3 / 4, "1E": 1 / 8, "21": 1 / 2, "22": 1 / 4, "2E": 1 / 4}

matrices = []
x = {"1": 7 / 8, "2": 1 / 16}
y = {"1": 1 / 8, "2": 15 / 16}

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


def HMM_V(time):
    for i in range(time + 1):
        matrices.append(np.matrix(np.arange(time * len(states)).reshape((time, len(states)))))
    return matrices


def HMM_R(state, current_time, current_prob):
    return HMM_R()

print(HMM_V(3))