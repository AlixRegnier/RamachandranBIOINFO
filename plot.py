import matplotlib.pyplot as plt
import numpy as np
from Point import Point

def draw_plot(name, windom_title, list_cluster_point):
    x=[]
    y=[]
    cluster=[]
    for i in range(0,len(list_cluster_point)):
        for point in list_cluster_point:
            if (point.id_cluster)*10 > 100:
                raise ValueError("Too many cluster, please not more than 10 cluster")
            x.append(point.get_abs())
            y.append(point.get_ord())
            cluster.append(int(point.id_cluster)*10)
    
    x=np.array(x)
    y=np.array(y)
    cluster=np.array(cluster)
    plt.xlabel("Φ angle")
    plt.ylabel("ψ angle")
    plt.xlim([-3.15, 3.15])
    plt.ylim([-3.15, 3.15])
    plt.gcf().canvas.manager.set_window_title(windom_title)
    plt.scatter(x,y,c=cluster,cmap="tab10")
    plt.title(name)
    plt.show()