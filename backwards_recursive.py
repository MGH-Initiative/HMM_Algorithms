import numpy as np

a = {'B':{'B':0, '1':1, '2':0, 'E':0}, '1':{'B':0, '1':0.125, '2':0.75, 'E':0.125}, '2':{'B':0,'1':0.5, '2':0.25, 'E':0.25},'E':{'B':0,'1':0, '2':0, 'E':0}}
e = {'1':{'X':7*0.125, 'Y':0.125}, '2': {'X':0.0625, 'Y':0.9375}}

nonsilent_states = ['1', '2']
silent_states = ['B', 'E']
end_vals = {'B':0,'1':0.125, '2':0.25, 'E':1}

def backwards(s,t, starting='B', maxtime = 4):
    nonsilent_sum = 0
    silent_sum = 0
    if starting:
        if s == starting and t > 0:
            return 0
    if t == maxtime:
        return end_vals[s]
    for k in nonsilent_states:
        nonsilent_sum += e[k]['X']*a[s][k]*backwards(k,t + 1)
    """
    for k in silent_states:
        silent_sum += a[s][k]*backwards(k,t)
    """
    return nonsilent_sum
        

def matrixifyBackwards(state_list, max_time, starting='B'):
    matrix = np.zeros((len(state_list), max_time+1))
    for state_i in range(len(matrix)):
        for time_i in range(max_time + 1):
            matrix[state_i,time_i] = backwards(state_list[state_i], time_i, starting=starting, maxtime = max_time)
    return matrix

state_list = ['B', '1', '2', 'E']

       
print("matrixifyBackwards(state_list, 4, starting='B')")
print(matrixifyBackwards(state_list, 4, starting='B'))
