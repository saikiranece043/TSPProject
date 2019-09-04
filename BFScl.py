from collections import defaultdict

class Graphbfscl:

    def __init__(self,vertices):
        self.vertices = vertices
        self.finalpaths = []
        self.graph = defaultdict(list)


    def addEdge(self,point,edge):
        self.graph[point].append(edge)

    def createData(self,data):
        for k,v in data:
           self.graph[k].append(v)

    def generatePaths(self,start,end):

        #create a queue to hold the list of paths
        queue =[]

        #push the start point into the queue

        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                print(path)
                self.finalpaths.append(path)

            for edge in self.graph.get(node,[]):
                new_path = list(path)
                new_path.append(edge)
                queue.append(new_path)


