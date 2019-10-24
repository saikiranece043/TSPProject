import math
import os
import logging
import time
import matplotlib.pyplot as plt
import sys

# %(asctime)s - %(name)s - %(levelname)s -
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(message)8s')


# Permutations of all the points excluding the starting point
# Input : list of points  Output : possible permutations list

def perm(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    permutations = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i + 1:]
        x = perm(remlst)
        for p in x:
            permutations.append([m] + p)
    return permutations


# Read from input .tsp file ,return the number of cities and stores the cities coordinates
# Input : data file Output : number of data inputs

def load(file):
    coordslist = []
    file = open(file, 'r')
    file.readline().strip().split()
    file.readline().strip().split()
    file.readline().strip().split()
    file.readline().strip().split()
    totalpoints = file.readline().strip().split()[1]
    file.readline().strip().split()
    file.readline().strip().split()
    for i in range(0, int(totalpoints)):
        x, y = file.readline().strip().split()[1:]
        coordslist.append([int(i), float(x), float(y)])

    return totalpoints, coordslist


# Calculate distance between 2 points given their coordinates as inputs
# Input : Two points a and b Output : distance between them

def dist(a, b, coordslist):
    xslope = coordslist[a - 1][1] - coordslist[b - 1][1]
    yslope = coordslist[a - 1][2] - coordslist[b - 1][2]
    temp = (xslope * xslope) + (yslope * yslope)
    return math.sqrt(temp)


# Load input values from the given .tsp


# Reads all the file names in given directory and returns the list of filenames
# Input : path of the directory Output : returns list of filenames
# This function isn't used for now as we are taking the data files as input args

def getAllFileNames(path):
    return os.listdir(path)


# Takes permutations,total points  and coordinates list as input
# Returns the shortest path routes as output

def modlist(data, coordslist):
    totaldist = 0
    shortestdist = 0
    iteration = 0
    shortestpath = []
    finalpathroutes = []
    print(coordslist)
    # print("Data points ",data)
    # print("Total Points ",totalpoints)
    # print("Coords list ",coordslist)
    # for p in [[ 2, 7, 6, 8, 5, 9, 10, 4, 3], [ 3, 4, 10, 9, 5, 8, 6, 7, 2]]:

    #the below for loop is to loop through the data after the generation of permutations
    #for p in perm(data):
    for p in data:
        #p.insert(0, 1)
        #p.insert(len(p), 1)

        for i in range(0, len(p) - 1):
            #print("Distance between point %s and point %s"%(p[i],p[i+1]))
            totaldist += dist(int(p[i]), int(p[i + 1]), coordslist)

        # logging.debug("Path: %s distance %f"%(p,totaldist))


        print("Path : " ,p ,"Total distance:" ,totaldist)
        if iteration == 0:
            shortestdist = totaldist

        #if "{0:.5f}".format(shortestdist) >= "{0:.5f}".format(totaldist):
        if shortestdist >= totaldist:
            shortestdist = totaldist
            shortestpath.append(p + [totaldist])
        # print("Total Distance: %f , Shortest Distance %f , Path %s" % (totaldist, shortestdist, p))
        # logging.debug("Total Distance: %f , Shortest Distance %f , Path %s" % (totaldist, shortestdist, p))

        totaldist = 0
        iteration += 1

    # logging.debug("Total number of paths %d"%iteration)
    print("Distance of the shortest path %f" % shortestdist)
    ##
    # logging.debug(shortestpath)

    for point in shortestpath:
        #if "{0:.5f}".format(float(point[len(point)-1])) == "{0:.5f}".format(shortestdist):
        if float(point[len(point)-1]) == shortestdist:
            finalpathroutes.append(point[:len(point)-1])
    return finalpathroutes


#This function takes totalpoints, coordslist and the shortestpath to plot a graph on x and y axis
#Input : totalpoints, coordslist , finalpath Output : The graph plotted saved as an image

def plotgraph(run,coordslist, finalpath):
    x = []
    y = []
    n = finalpath

    plt.ioff()

    # if( iter !=0 ):
    #     plt.clf()

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)


    for point in finalpath:
        #print(point)
        index = int(point) -1
        x.append(coordslist[index][1])
        y.append(coordslist[index][2])


    #This is for backtracking the graph to the starting point to form a cylce
    # x.append(coordslist[0][1])
    # y.append(coordslist[0][2])
    plt.plot(x, y, color='green', linewidth=1,
             marker='o', markerfacecolor='blue', markersize=5)

    # for xy in zip(x, y):  # <--
    #     i=0;
    #     ax.annotate('(%s, %s)' %xy, xy=xy, textcoords='data')  # <--
    #     i+=1

    for i, n in enumerate(n):
        ax.annotate(n, (x[i], y[i]), textcoords='data')


    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.savefig('Random' + str(run) + ".png")
    #print("Plotted a graph for the shortest route Random%s.png\n" % totalpoints)






# Displays how the program is to be executed if there are no args passed to the program

def usage():
    print("This program would need atleast one argument\n")
    print("The argument is the location of the input file in .tsp format(one or more paths allowed)\n")
    print("Ex: Python TSPSol.py 'filepath1' 'filepath2' \n")
    sys.exit(0)


#main function to invoke all the required functions to solve the program as a whole
# Inputs : None Output : shortest path

def main():
    # files = getAllFileNames('../tspfiles')
    # files = ["Random4.tsp", "Random5.tsp", "Random6.tsp", "Random7.tsp", "Random8.tsp", "Random9.tsp", "Random10.tsp","Random11.tsp"]
    # files=["../tspfiles/Random8.tsp"]
    # print(sys.argv)
    files = []

    if len(sys.argv) < 2:
        usage()

    else:
        for argnum in range(len(sys.argv) - 1):
            files.append(sys.argv[argnum + 1])


    for file in files:
        finalpath = []
        print("Solving TSP problem based on data in file located at path %s" % file)
        totalpoints, coordslist = load(file)
        data = list(range(2, int(totalpoints) + 1))
        finalpath = modlist(data, totalpoints, coordslist)
        print("Shortest Paths: ", finalpath)
        plotgraph( coordslist, finalpath[0])
        # time.sleep(6)

# totalpoints= load('Random10.tsp')
# data = list(range(2, int(totalpoints) + 1))
# modlist(data, totalpoints)



if __name__ == '__main__':
    start_time = time.time()
   # main()

    print("--- %s seconds taken to execute the program---" % (time.time() - start_time))
