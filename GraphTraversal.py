import sys
import time

sys.path.insert(0, '../src/com/uofl/edu')
from TSPSol import load, modlist, plotgraph
import BFScl
import DFS


def usage():
    print("Please do run the program as below with mandatory args")
    print("Ex: python GraphTraversal 'inputfile' 'traversaltype' ")




def main():
    files = []

    if len(sys.argv) < 3:
        usage()

    else:

        datainputfile = sys.argv[1]
        traversaltype = sys.argv[2]


        # datainputfile = '11PointDFSBFS.tsp'
        # traversaltype = 'BFS'

        totalpoints, coordlist = load(datainputfile)

        if (traversaltype == 'BFS'):

            print("Using Traversal type : Breadth First Search Algorithm to find the shortest path")
            print("Below are the list of all possible traversal paths and we are going to find shortest route among them")

            # Creating a BFScl object and storing the graph data in the object property

            g = BFScl.Graphbfscl(11)
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

            # Generating all possible paths by invoking the object member function

            g.generatePaths(1,11)

            # reusing project1 code to calculate distance for list of paths and find shortest of all

            shortroute = modlist(g.finalpaths, totalpoints, coordlist)
            print("Shortest path using BFS Algorithm: ", shortroute)


        if (traversaltype == 'DFS'):
            print("Using Traversal type : Depth First Search Algorithm to find the shortest path")
            print("Below are the list of all possible traversal paths and we are going to find shortest route among them")

            # Creating a DFS object and storing the graph data in the object property

            g = DFS.Graph(11)
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

            graphdata = [[2, 3, 4],[3],[4, 5],[5, 6, 7],[7, 8],[8],[9, 10],[9, 10, 11],[11]]
            # Generating all possible paths by invoking the object member function
            print(g.graph)
            g.getAllPaths(1, 11)

            # reusing project1 code to calculate distance for list of paths and find the shortest of all

            shortroute = modlist(g.finalpaths, totalpoints, coordlist)
            print("Shortest path using DFS Algorithm: ", shortroute)

            plotgraph(totalpoints, coordlist, shortroute[0])

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds taken to execute the program---" % (time.time() - start_time))
