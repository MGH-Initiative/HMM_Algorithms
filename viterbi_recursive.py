import numpy as np

a = {'B':{'B':0, '1':1, '2':0, 'E':0}, '1':{'B':0, '1':0.125, '2':0.75, 'E':0.125}, '2':{'B':0,'1':0.5, '2':0.25, 'E':0.25},'E':{'B':0,'1':0, '2':0, 'E':0}}
e = {'B':{'X':1, 'Y':1}, '1':{'X':7*0.125, 'Y':0.125}, '2': {'X':0.0625, 'Y':0.9375}}

nonsilent_states = ['1','2']
silent_states = ['B','E']

seq = [0,'X','X','X','X']

"""
NOTE: you must indicate your starting node even if it's silent, so that it can
be counted as a nonsilent_state just for time == 1
"""
def viterbi(state, time, starting=None):
    nss = list(nonsilent_states)
    if not time: #lazy way of saying time == 0
        return int(state == starting)
    if time and starting and state in nonsilent_states:
        nss.append(starting)
    if state in nonsilent_states:
         return e[state][seq[time]] * max([a[x][state] * viterbi(x, time-1, starting=starting) for x in nss])
    else:
        return max([a[x][state] * viterbi(x, time, starting=starting) for x in nss])

def matrixifyViterbi(state_list, max_time, starting='B'):
    matrix = np.zeros((len(state_list), max_time+1))
    for state_i in range(len(matrix)):
        for time_i in range(max_time + 1):
            matrix[state_i,time_i] = viterbi(state_list[state_i], time_i, starting=starting)
    return matrix

state_list = ['B', '1', '2', 'E']

print("matrixifyViterbi(state_list, 4, starting='B')")
print(matrixifyViterbi(state_list, 4, starting='B'))
