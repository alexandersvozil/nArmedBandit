from __future__ import division
import numpy as np
import random
import visualization as v
def useLever(b_levers,a):
    noise = np.random.normal(0.0,1.0,1)
    return b_levers[a]+noise


def calcQ_t(Q_t,a,reward,stepsize):
#    print str(stepsize) + " " + str(a) + " " + str(reward) + " " + str(Q_t[a]) +" "+ str(Q_t)
    Q_t[a] = Q_t[a] + stepsize * (reward - Q_t[a])
    return Q_t

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
            assert (str(np.sum(probA)) == str(1.0))
            return np.argmax(np.random.multinomial(1,probA,1))
        else:
            return np.argmax(Q_t)


def testbed(eps,temp,levers,testbedNr,randomWalks,stepsize):
    avgReward = np.zeros((1000,testbedNr))
    bestLeverused = np.zeros((1000,testbedNr))
    for i in range(0,testbedNr):
        b_levers = levers[:,i]
        optimal_lever = np.argmax(b_levers)
        times = np.zeros(10)
        Q_t = np.zeros(10)
        rewardsum = 0
        for t in range(0, 1000):
            #if we enable random walk change levers every 30th time we pull on a lever
            if(randomWalks and ((t+1) % 200 == 0)):
                b_levers = np.random.standard_normal(10)
                optimal_lever = np.argmax(b_levers)

            #choose lever
            a  = greedyDecision(Q_t,eps,temp)
            reward = useLever(b_levers,a)
            #calculate Q_t
            times[a] = times[a]+1
            if(stepsize == 0):
                Q_t = calcQ_t(Q_t,a,reward,(1/times[a]))
            if(stepsize > 0):
                Q_t = calcQ_t(Q_t,a,reward,stepsize)
            #for the graphs
            rewardsum += reward

            #save the average reward for timestamp t and best action used
            bestLeverused[t,i] = times[optimal_lever]/(t+1)
            avgReward[t,i] = rewardsum/(t+1)
     #   print "eps: " +str(eps)+ "\nQ_T: " + str(Q_t) + "\nLevers: " + str(b_levers)
    return (avgReward,bestLeverused)

testbedNr =200
levers = np.random.standard_normal((10,testbedNr))
#generate testbeds
#(avgReward,bL) = testbed(0,0,levers,testbedNr,False,0)
#(avgRewardg1,bL1) = testbed(0.1,0,levers,testbedNr,False,0)
#(avgRewardg2,bL2) = testbed(0.01,0,levers,testbedNr,False,0)
#(avgRewardg3,bL3) = testbed(0.1,1,levers,testbedNr,False,0)
#(avgRewardg4,bL4) = testbed(0.1,1,levers,testbedNr,False,0.1)
#
#avgRew  = [(avgReward,'greedy','green'),(avgRewardg1,'0.1','black'),(avgRewardg2,'0.01','red'),(avgRewardg3,'0.1+boltz','orange'), (avgRewardg4,'0.1+boltz+constantstep','magenta')]
#avgBL   = [(bL,'greedy','green'),(bL1,'0.1','black'),(bL2,'0.01','red'),(bL3,'0.1+boltz','orange'),(bL4, '0.1+boltz+constantstep', 'magenta')]
#avgRew  = [(avgReward,'greedy','green'),(avgRewardg1,'0.1','black'),(avgRewardg2,'0.01','red'),(avgRewardg3,'0.1+boltz','orange')]
#avgBL   = [(bL,'greedy','green'),(bL1,'0.1','black'),(bL2,'0.01','red'),(bL3,'0.1+boltz','orange')]
#v.vis_matplot(avgRew,avgBL)

(avgReward,bL) = testbed(0,0,levers,testbedNr,True,0)
(avgRewardg1,bL1) = testbed(0.1,0,levers,testbedNr,True,0)
(avgRewardg2,bL2) = testbed(0.01,0,levers,testbedNr,True,0)
(avgRewardg3,bL3) = testbed(0.1,1,levers,testbedNr,True,0)
(avgRewardg4,bL4) = testbed(0.1,1,levers,testbedNr,True,0.3)
avgRew  = [(avgReward,'greedy','green'),(avgRewardg1,'0.1','black'),(avgRewardg2,'0.01','red'),(avgRewardg3,'0.1+boltz','orange'), (avgRewardg4,'0.1+boltz+constantstep','magenta')]
avgBL   = [(bL,'greedy','green'),(bL1,'0.1','black'),(bL2,'0.01','red'),(bL3,'0.1+boltz','orange'),(bL4, '0.1+boltz+constantstep', 'magenta')]
v.vis_matplot(avgRew,avgBL)

#visualize





