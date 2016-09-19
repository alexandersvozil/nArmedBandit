import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import random

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

def greedyDecision(Q_t,eps):
    #greedily chose lever with highest index
    if eps == 0:
        return np.argmax(Q_t)
    else:
        explore = np.random.binomial(1,eps,1)
        if(explore == 1):
           return random.randint(0,9)
        else:
            return np.argmax(Q_t)


def testbed(eps):
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
            a  = greedyDecision(Q_t,eps)
            times[a] = times[a]+1
            reward = useLever(b_levers,a)
            R_t[a,t] = reward
            #save the average reward for timestamp t
            bestLeverused[t,i] = times[optimal_lever]/(t+1)
            avgReward[t,i] = np.sum(R_t)/(t+1)
    return (avgReward,bestLeverused)
#generate banditlevers
avg_x = np.linspace(0,1000,1000)
(avgReward,bL) = testbed(0)
(avgRewardg1,bL1) = testbed(0.1)
(avgRewardg2,bL2) = testbed(0.01)



avgAvgReward = np.average(avgReward,1)
trace1 = go.Scatter(
    x = avg_x,
    y = avgAvgReward,
    mode = 'lines+markers',
    name = 'Greedy',
    marker= dict(
        size = 2,
        color = 'green'
    )
)
avgAvgRewardg1 = np.average(avgRewardg1,1)
trace2= go.Scatter(
    x = avg_x,
    y = avgAvgRewardg1,
    mode = 'lines+markers',
    name = 'epsilon = 0.1',
    marker= dict(
        size = 2,
        color = 'black'
    )
)
avgAvgRewardg2 = np.average(avgRewardg2,1)
trace3 = go.Scatter(
    x = avg_x,
    y = avgAvgRewardg2,
    mode = 'lines+markers',
    name = 'epsilon = 0.01',
    marker= dict(
        size = 2,
        color = 'red'
    )
)

avgbL = np.average (bL,1)
avgbL1 = np.average(bL1,1)
avgbL2 = np.average(bL2,1)
trace4 = go.Scatter(
    x = avg_x,
    y = avgbL,
    mode = 'lines+markers',
    name = 'Greedy',
    marker= dict(
        size = 2,
        color = 'green'
    )
)
trace5= go.Scatter(
    x = avg_x,
    y = avgbL1,
    mode = 'lines+markers',
    name = 'epsilon = 0.1',
    marker= dict(
        size = 2,
        color = 'black'
    )
)
trace6 = go.Scatter(
    x = avg_x,
    y = avgbL2,
    mode = 'lines+markers',
    name = 'epsilon = 0.01',
    marker= dict(
        size = 2,
        color = 'red'
    )
)

data = [trace1,trace2,trace3]
data2 = [trace4,trace5,trace6]
py.plot(data,filename='avgReward')
py.plot(data2,filename='avgBestDecision')



#visualize


