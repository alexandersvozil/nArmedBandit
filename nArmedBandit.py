import numpy as np
import random
import visualization as v
def useLever(b_levers,a):
    noise = np.random.normal(0.0,1.0,1)
    return b_levers[a]+noise

#credits to denis http://stackoverflow.com/questions/26248654/numpy-return-0-with-divide-by-zero
def div0( a, b ):
    """ ignore / 0, div0( [-1, 0, 1], 0 ) -> [0, 0, 0] """
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 0  # -inf inf NaN
    return c

def calcQ_t(R_t, timesLeverused):
    return div0(np.sum(R_t,1),timesLeverused)

def greedyDecision(Q_t,eps,temp):
    #if our exploration probability is zero, greedily chose lever with highest index
    if eps == 0:
        return np.argmax(Q_t)
    else:
    #otherwise explore with probability eps
        explore = np.random.binomial(1,eps,1)
        if(explore == 1 and temp == 0):
           return random.randint(0,9)
        elif (explore == 1 and temp > 0):
            probA = np.divide(np.exp(np.divide(Q_t,temp)), np.sum(np.exp(np.divide(Q_t,temp))))
            #print probA
            #print "sum:" + str(np.sum(probA))
            assert (str(np.sum(probA)) == str(1.0))

            return np.argmax(np.random.multinomial(1,probA,1))
        else:
            return np.argmax(Q_t)


def testbed(eps,temp):
    testbedNr = 500
    avgReward = np.zeros((1000,testbedNr))
    bestLeverused = np.zeros((1000,testbedNr))
    for i in range(0,testbedNr):
        b_levers = np.random.standard_normal(10);
        optimal_lever = np.argmax(b_levers)
        R_t = np.zeros((10,1000))
        times = np.zeros(10)
        for t in range(0, 1000):
            #calculate Q_t
            Q_t = calcQ_t(R_t,times)

            #choose decision algorithm
            a  = greedyDecision(Q_t,eps,temp)
            times[a] = times[a]+1
            reward = useLever(b_levers,a)
            R_t[a,t] = reward
            #save the average reward for timestamp t
            bestLeverused[t,i] = times[optimal_lever]/(t+1)
            avgReward[t,i] = np.sum(R_t)/(t+1)
    return (avgReward,bestLeverused)
#generate banditlevers
(avgReward,bL) = testbed(0,0)
(avgRewardg1,bL1) = testbed(0.1,0)
(avgRewardg2,bL2) = testbed(0.01,0)
(avgRewardg3,bL3) = testbed(0.1,1)

avgRew  = [(avgReward,'greedy','green'),(avgRewardg1,'0.1','black'),(avgRewardg2,'0.01','red'),(avgRewardg3,'0.1+boltz','orange')]
avgBL   = [(bL,'greedy','green'),(bL1,'0.1','black'),(bL2,'0.01','red'),(bL3,'0.1+boltz','orange')]
v.vis(avgRew,avgBL)


#visualize





