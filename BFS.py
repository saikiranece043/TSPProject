from src.com.uofl.edu import TSPSol


# graph is in adjacent list representation


graph = {
        '1': ['2', '3', '4'],
        '2': ['3'],
        '3': ['4', '5'],
        '4': ['5', '6', '7'],
        '5': ['7', '8'],
        '6' : ['8'],
        '7' : ['9','10'],
        '8' : ['9','10','11'],
        '9' : ['11']
        }

finalpaths =[]

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            finalpaths.append(path)

        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)



bfs(graph, '1', '11')
totalpoints,coordlist = TSPSol.load('11PointDFSBFS.tsp')
shortroute = TSPSol.modlist(finalpaths,totalpoints,coordlist)
print("Shortest path using DFS Algorithm: ",shortroute)
TSPSol.plotgraph(totalpoints,coordlist,shortroute[0])