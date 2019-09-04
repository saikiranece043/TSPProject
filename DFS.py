# Python program to print all paths from a source to destination.


from collections import defaultdict

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


    def createData(self,data):
        for k,v in data:
           self.graph[k].append(v)

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
            print(path)
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




