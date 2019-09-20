import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import threading
from TSPSol import load, modlist,dist
import time
from math import acos,degrees,sqrt
import sys



inputdatafile = 'Random40.tsp'
totalpoints,coordlist=load(inputdatafile)

tourpath=[]
tourstatus= False
totalpointsInt = int(totalpoints)
possibletourpath = list(range(1,totalpointsInt+1))

#first path in the tour is 1
#16,17 starting point has been the best so far 6,25 -- 16,10
startingpoint=6
secondpoint=25



tourpath.append(startingpoint)
tourpath.append(secondpoint)




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






# def distofpointfromedge(a,b,point):
#     # xslope = coordlist[a - 1][1] - coordlist[b - 1][1]
#     # yslope = coordlist[a - 1][2] - coordlist[b - 1][2]
#     #
#     # xspoint= coordlist[point-1][1]
#     # yspoint = coordlist[point-1][2]
#     #
#     # temp = (xslope * xslope) + (yslope * yslope)
#     # denominator = math.sqrt(temp)
#     # numerator = (xslope * (coordlist[a-1][2]- yspoint)) - ((coordlist[a-1][1]-xspoint) * yslope)
#     # return abs(numerator/denominator)
#
#     #different method for calculating height of triangle i.e shortest distance
#     side1= dist(a,b,coordlist)
#     side2= dist(a,point,coordlist)
#     side3= dist(b,point,coordlist)
#
#     perimeter = (side1+side2+side3)/2
#     area = math.sqrt(perimeter * (perimeter-side1) * (perimeter-side2) * (perimeter - side3) )
#     return 2*(area/side1)

    #The area of the parallelogram spanned by points 𝐴,𝐵 (on the line), and 𝐶 is


    # base = dist(a,b,coordlist)
    #
    # diff1 = (coordlist[b-1][1] - coordlist[a-1][1])* (coordlist[point-1][2] - coordlist[a-1][2])
    # diff2 = (coordlist[b-1][2] - coordlist[a-1][2])* (coordlist[point-1][1] - coordlist[a-1][1])
    #
    # area = abs(diff1 - diff2)
    # return area/base


# def distofpointfromedge(a,b,point):
#     xa = coordlist[a-1][1]
#     ya= coordlist[a-1][2]
#     xb = coordlist[b-1][1]
#     yb = coordlist[b-1][2]
#     xp = coordlist[point-1][1]
#     yp= coordlist[point-1][1]
#
#     a = xp - xa
#     b = yp - ya
#     c = xb - xa
#     d = yb - ya
#
#     dot = a * c + b * d
#     len_sq = c * c + d * d
#     param = -1
#
#     if len_sq != 0:
#         param = dot/len_sq
#
#     if param < 0:
#         xx = xa
#         yy = ya
#         edgeside = "left"
#
#     elif param > 1:
#         xx = xb
#         yy = yb
#         edgeside = "right"
#
#     else:
#         xx = xa + param * c
#         yy = ya + param * d
#         edgeside = "center"
#     dx = xp - xx
#     dy = yp - yy
#
#     return math.sqrt(dx*dx+dy*dy),edgeside










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
                     print("Distance between point %d, edge %s, %s tourpath  %f distance " % (i, edge,tourpath,distance))
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


    print("Shortest distance from the edge %s to point %d is %f"%(shortdistance[3],shortdistance[1],shortdistance[0]))
    #print("Current tour path ",tourpath)
    return shortdistance,tourstatus





# Visual representaiton of the tour



style.use('ggplot')
fig = plt.figure()
ax1= fig.add_subplot(1,1,1)

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





# def plotpoints():
#     xs = []
#     ys = []
#     for point in possibletourpath:
#         # print(point)
#         index = int(point) - 1
#         xs.append(coordlist[index][1])
#         ys.append(coordlist[index][2])
#
#     plt.plot(xs, ys, color='green', linewidth=0, marker='o', markerfacecolor='blue', markersize=5)
#
#     # for xy in zip(x, y):  # <--
#     #     i=0;
#     #     ax.annotate('(%s, %s)' %xy, xy=xy, textcoords='data')  # <--
#     #     i+=1
#
#     for i, n in enumerate(possibletourpath):
#          ax1.annotate((n,0, 0), (xs[i],ys[i]), textcoords='data')
#
#     plt.xlabel('x-axis')
#     plt.ylabel('y-axis')
#
#     plt.savefig('Random' + totalpoints + "pointsplot.png")



#
# next=findnextpointontour(1,tourpath)[1]
# while(next):
#     time.sleep(5)
#     print("Next path on the TSP tour is %d"%next)
#     tourpath.append(next)
#     next=findnextpointontour(next,tourpath)[1]

def usage():
    print("Ex: python WebSocketInt Random40.tsp")


def main():
    if len(sys.argv) < 1:
        usage()

    else :
        inputdatafile = sys.argv[1]


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds taken to execute the program---" % (time.time() - start_time))
