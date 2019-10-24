import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import threading
from TSPSol import load, modlist,dist
import time
from math import acos,degrees,sqrt



#Global variables declared below

#TSP Input file
inputdatafile = 'Random222.tsp'

#data loaded from the input file
totalpoints,coordlist=load(inputdatafile)

#inital tour path is set to null
tourpath=[]

#tour completion status as False initially
tourstatus= False

#total number of points in the input file is converted to int
totalpointsInt = int(totalpoints)

#an array which holds one possible tour path
possibletourpath = list(range(1,totalpointsInt+1))

#first path in the tour is 1
#16,17 starting point has been the best so far 6,25 -- 16,10
startingpoint=random.sample(possibletourpath,1).pop()




def getSecondPoint(startingpoint):
    iter = 0
    for city in possibletourpath:
        if city != startingpoint:
           dista = dist(city,startingpoint,coordlist)
        if iter == 0:
           sdist = dista
           secondcity = city
        if sdist > dista:
           sdist = dista
           secondcity = city
        iter+=1
    return secondcity


secondpoint=getSecondPoint(startingpoint)



getSecondPoint(startingpoint)

# appending the first and second city to the touor
tourpath.append(startingpoint)
tourpath.append(secondpoint)


print(startingpoint)

#returns the distance of the point from the line segment from by a,b and also suggests if the point is close to a or b or the line segment
def isperpendicular(a,b,point):
     a1= dist(b,point,coordlist)
     b1= dist(a,point,coordlist)
     c1=dist(a,b,coordlist)

     numa=( b1*b1 + c1*c1 - a1*a1)
     dena= 2*b1*c1

     angleA=degrees(acos(numa/dena))
     #print("AngleA ",angleA)


     numb = (a1*a1 + c1*c1 - b1*b1)
     denb = 2*a1*c1

     angleB=degrees(acos(numb/denb))
     #print("AngleB", angleB)

     if angleA >= 90:
         closestpoint = "leftp"
         distance = a1

     elif angleB >=90:
         closestpoint = "rightp"
         distance = b1

     else:
         closestpoint = "edge"
         perimeter = (a1 + b1 + c1)/2
         area = sqrt(perimeter * (perimeter-a1) * (perimeter-b1) * (perimeter - c1) )
         distance=2*(area/c1)


     return distance,closestpoint




#Helps finding the next city on tour based on how close is to the list of edges formed by current cities on tour
def findnextpointontour(tourpath):
    shortdistance=[0,0,0,0]
    iteration=1
    edges=[]
    length = len(tourpath)
    for idx in range(len(tourpath)-1):
        edges.append([tourpath[idx],tourpath[idx+1]])
    print(edges)

    for i in range(1,totalpointsInt+1):
        for edge in edges:
            if i not in tourpath:

                     #Euclidean Distance between 2 points to find the closet point from the one's on the tour
                     distance,closestpoint=isperpendicular(edge[1],edge[0],i)
                     #distance=dist(tourpath[length-1],i,coordlist)
                     #print("Distance from edge [%d,%d] to point %d is %f"%(tourpath[length-2],tourpath[length-1],i,distance))
                     #print("Distance between point %d, edge %s, %s tourpath  %f distance " % (i, edge,tourpath,distance))
                     if  iteration ==1 :
                         shortdistance[0]=distance
                         shortdistance[1]=i
                         shortdistance[2]=closestpoint
                         shortdistance[3]=edge
                     if  shortdistance[0] > distance:
                         shortdistance[0]=distance
                         shortdistance[1]= i
                         shortdistance[2]= closestpoint
                         shortdistance[3]=edge
                     iteration += 1

    tourstatus = all(elem in tourpath for elem in possibletourpath)


    #print("Shortest distance from the edge %s to point %d is %f"%(shortdistance[3],shortdistance[1],shortdistance[0]))
    #print("Current tour path ",tourpath)
    return shortdistance,tourstatus





# Visual representaiton of the tour



style.use('ggplot')
fig = plt.figure()
ax1= fig.add_subplot(1,1,1)


# this function is to provide a live plotting of the selection of the cities on the tour one by one
# this function displays how the cities are selected one by one visually on a 2 dimensional space
def animate(i):
    xs = []
    ys = []

    print(tourpath)

    next, tourstatus = findnextpointontour(tourpath)
    lenghtofpath = len(tourpath)
    if tourstatus:

        tourpath.append(tourpath[0])
        print(tourpath)

    else:

        #tourpath.append(next[1])
        #print("insertion of the point on the right side of the edge",tourpath)

        if next[2] == "leftp":
            #tourpath.insert(lenghtofpath-2,next[1])

            print("the shortest path to the point %d lies to the left of the edge %s"%(next[1],next[3]))
            index=tourpath.index(next[3][0])
            tourpath.insert(index,next[1])
            print("insertion of the point on the left side of the edge",tourpath)

        elif next[2] == "rightp":
            print("the shortest path to the point %d lies to the right of the edge %s" % (next[1],next[3]))
            index = tourpath.index(next[3][1])
            #tourpath.append(next[1])
            tourpath.insert(index+1,next[1])
            print("insertion of the point on the right side of the edge",tourpath)



        elif next[2] == "edge":
            print("the shortest path to the point %d lies near the edge %s" % (next[1],next[3]))
            #tourpath.insert(lenghtofpath-1,next[1])
            index = tourpath.index(next[3][1])
            tourpath.insert(index,next[1])
            print("insertion of the point on the middle of the edge",tourpath)


    print(tourpath)

    for point in tourpath:
        # print(point)
        index = int(point) - 1
        xs.append(coordlist[index][1])
        ys.append(coordlist[index][2])

    ax1.clear()
    #ax1.plot(xs,ys)
    plt.plot(xs, ys, color='green', linewidth=1,  marker='o', markerfacecolor='blue', markersize=5)

    # for xy in zip(x, y):  # <--
    #     i=0;
    #     ax.annotate('(%s, %s)' %xy, xy=xy, textcoords='data')  # <--
    #     i+=1

    for i, n in enumerate(tourpath):
        ax1.annotate(n, (xs[i], ys[i]), textcoords='data')
        #ax1.annotation('textarrow', xs[i], ys[i])


    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    if tourstatus:
        modlist([tourpath],coordlist)
        plt.savefig('Random' + totalpoints + ".png")
        plt.show()
        time.sleep(5)
        quit(0)
 #print("Plotted a graph for the shortest route Random%s.png\n" % totalpoints)



ani = animation.FuncAnimation(fig,animate,interval=1000)



plt.show()



