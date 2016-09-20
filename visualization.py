import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt

def vis_matplot(avgReward,avgBL):
    data_rew = list()
    data_bl = list()

    avg_x = np.linspace(0,1000,1000)

    for (avgR,name,color) in avgReward:
        avgAvgR = np.average(avgR,1)
        plt.plot(avg_x,avgAvgR,c=color,linewidth=2,label=name)
    plt.legend()
    plt.show()


    for (abl,name,color) in avgBL:
        avgAvgBL = np.average(abl,1)
        plt.plot(avg_x,avgAvgBL,c=color,linewidth=2,label=name)
    plt.legend()
    plt.show()
    return

def vis(avgReward,avgBL):
    data_rew = list()
    data_bl = list()

    avg_x = np.linspace(0,1000,1000)
    for (avgR,name,color) in avgReward:
      avgAvgR = np.average(avgR,1)
      trace = go.Scatter(
          x = avg_x,
          y = avgAvgR,
          mode = 'lines+markers',
          name = name,
          marker= dict(
              size = 2,
              color =color
          )
      )
      data_rew.append(trace)

    for (abl,name,color) in avgBL:
        avgAvgBL = np.average(abl,1)
        trace = go.Scatter(
            x = avg_x,
            y = avgAvgBL,
            mode = 'lines+markers',
            name = name,
            marker= dict(
                size = 2,
                color =color
            )
        )
        data_bl.append(trace)
    py.image.save_as(data_rew,filename='avgReward.png')
    py.image.save_as(data_bl,filename='avgBestDecision.png')
