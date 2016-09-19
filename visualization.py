import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

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
    py.plot(data_rew,filename='avgReward')
    py.plot(data_bl,filename='avgBestDecision')
