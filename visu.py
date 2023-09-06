import matplotlib.pyplot as plt
import numpy as np
from Point import Point



def draw_plot(list_list):
    x=[]
    y=[]
    cluster=[]
    for i in range(0,len(list_list)):
        for point in list_list[i]:
            x.append(point.get_abs())
            y.append(point.get_ord())
            cluster.append(i*10)
    
    x=np.array(x)
    y=np.array(y)
    cluster=np.array(cluster)

    plt.scatter(x,y,c=cluster,cmap="Accent")

    plt.show()

if __name__ == "__main__":
    with open("angles_1TEY_small_clust.txt","r") as in_file:
        cluster_1=[]
        cluster_2=[]
        cluster_3=[]
        cluster_4=[]
        for line in in_file:
            if line[0]!="p":
                x=float(line.split("\t")[0])
                y=float(line.split("\t")[1])
                if line.split("\t")[2]=="1\n":
                    cluster_1.append(Point(x,y))
                if line.split("\t")[2]=="2\n":
                    cluster_2.append(Point(x,y))
                if line.split("\t")[2]=="3\n":
                    cluster_3.append(Point(x,y))
                if line.split("\t")[2]=="4\n":
                    cluster_4.append(Point(x,y))
                

    draw_plot([cluster_1,cluster_2,cluster_3,cluster_4])