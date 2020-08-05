import math as m 
import matplotlib.pyplot as plt

coords = []

def plotIt(coords):
    xPoints = coords[0]
    yPoints = coords[1]
    zPoints = coords[2]
    tPoints = coords[3]

    plt.plot(xPoints, tPoints)
    plt.plot(yPoints, tPoints)
    plt.plot(zPoints, tPoints)

