# Python program to print all paths from a source to destination.


from collections import defaultdict
from src.com.uofl.edu import TSPSol

# This class represents a directed graph
# using adjacency list representation


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.graph = defaultdict(list)
        # default dictionary to store graph
        self.finalpaths = []
        self.counter = 0

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def getAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]

        if u == d:
            temp = list(path)
            self.finalpaths.append(temp)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.getAllPathsUtil(i, d, visited, path)

                    # Remove current vertex from path[] and mark it as unvisited

        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def getAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V + 2)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.getAllPathsUtil(s, d, visited, path)

    # Create a graph given in the above diagram


g = Graph(11)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 7)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(6, 8)
g.addEdge(7, 9)
g.addEdge(7, 10)
g.addEdge(8, 9)
g.addEdge(8, 10)
g.addEdge(8, 11)
g.addEdge(9, 11)

#print(g.graph)

s = 1
d = 11
print("Following are all different paths from %d to %d :" % (s, d))

g.getAllPaths(s, d)
#print(g.finalpaths)
totalpoints,coordlist = TSPSol.load('11PointDFSBFS.tsp')


shortroute = TSPSol.modlist(g.finalpaths,totalpoints,coordlist)
print("Shortest path using DFS Algorithm: ",shortroute)

TSPSol.plotgraph(totalpoints,coordlist,shortroute[0])