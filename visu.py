import matplotlib.pyplot as plt
import numpy as np
from Point import Point



def draw_plot(list_cluster_point,type):
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
    
    if type == "chi":
        plt.xlabel("Chi1 angle")
        plt.ylabel("Chi2 angle")
    if type == "phi":
        plt.xlabel("Φ angle")
        plt.ylabel("ψ angle")


    plt.scatter(x,y,c=cluster,cmap="tab10")

    plt.show()
