import numpy

np = numpy

###################################################

# initialized and defined set of all potential states

states = {"B", "1", "2", "E"}

start_state = "B"

emissions = {"x", 'y'}

# dictionaries with transitory probabilities ( the title is the destination and the key is the starting location)
#   ex: dictionary named "one" holds keys to all the transition probabilities of going from other states TO one

# why do we need a dictionary? I just put the values in order from B to E
b = [0,0,0,0];
one = [1,1/8,1/2,/0]
two = [0,3/4,1/4,0]
e= [0,1/8,1/4,0]

# lulu not using the following:
#b = {"B":0, "1":0, "2":0, "E":0}
#one = {"B":1, "1":1/8, "2":1/2, "E":0}
#two = {"B":0, "1":3/4, "2":1/4,"E":0}
#e = {"B":0, "1":1/8, "2":1/4, "E":0}
#all = {"B" : b, "1" : one, "2" : two, "E" : e}
allStates = [b, one, two, e] # a vector of vectors

# dictionary with the respective probabilities for emitted states x and y

x = {"1": 7 / 8, "2": 1 / 16}

y = {"1": 1 / 8, "2": 15 / 16}

#####################################################

# function that specifies all the base cases

def hmm_v(state, time): #state is char and time is int

    # three dimensional matrix that represents the table provided in the paper

    matrix = np.zeros((len(emissions), len(states), time + 1))

    matrix[:, 0, 0 ] = 1

    for i in range(1, time + 1): #this loops thru timeCourses
        for st in range(0, len(states)):
            if i==time+1: #the target time
                #go thru only the input "state" b/c u don't need to consider it going thru all the states at the target time
                tempProbsX = np.zeros[len(states)]
                tempProbsY = np.zeros[len(states)]
                stateIndex = states.index(state)
                currStateTrans = allStates[stateIndex]
                for f in range(0,len(states)):
                    stateNum = stateIndex + ""
                    tempProbsX[f] = currStateTrans[f]*matrix[0,f,i-1]*x{stateNum}
                    tempProbsY[f] = currStateTrans[f]*matrix[1,f,i-1]*y{stateNum}
                maxProbX = max(tempProbsX)
                maxProbY = max(tempProbsY)
                matrix[0,stateIndex,i] = maxProbX
                matrix[1,stateIndex,i] = maxProbY
                Xprob = matrix[0,stateIndex,i]
                Yprob = matrix[1,stateIndex,i] 
                return [Xprob,Yprob]
            else:
                for j in range (0,len(states)): #this loops thru all states in the current time course
                    tempProbsX = np.zeros[len(states)] #holds all probabilities for current state X emission. Take the max of this to assign value for that state
                    tempProbsY = np.zeros[len(states)] #same but for Y emission
                    transitions = allStates[j] #finds the vector for the trans probs to the current state
                    maxProbX = 0
                    maxProbY = 0
                    for m in range (0,len(states)): #this loops thru all the prev states and their transitions to the current state at j
                        stateNum = j+""
                        tempProbsX[m] = matrix[0,m,i-1]*transitions[m]*x{stateNum}
                        tempProbsY[m] = matrix[1,m,i-1]*transitions[m]*y{stateNum}
                    maxProbX = max(tempProbsX)
                    maxProbY = max(tempProbsY)
                    matrix[0,j,i] = maxProbX
                    matrix[1,j,i] = maxProbY
                    
                                           
                                           
                                           
                        
                    #calc probability for all of the states in the current time
                    # use "all" to go thru all dictionaries, corresponding to the states
                    
         # lulu in progress code:
         # the idea is that for every current state in a time course:
         # you go through all the previous states of the last time course
         # and multiply by their transitions to the current state
         # then take the max of these values for the one matrix[x,y,z] value
        for value in all.items():
            print(value)








print(hmm_v("B", 4))
