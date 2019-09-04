from flask import Flask,jsonify
#import sys
#sys.path.insert(0, '../src/com/uofl/edu')

from src.com.uofl.edu import DFS
from src.com.uofl.edu import BFScl
from src.com.uofl.edu import TSPSol
app = Flask(__name__)

print(__name__)

totalpoints,coordslist = TSPSol.load('11PointDFSBFS.tsp')


@app.route('/DFS')
def dfs():
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

    g.getAllPaths(1, 11)

    shortroute= TSPSol.modlist(g.finalpaths,totalpoints,coordslist)
    return jsonify({'routes' : g.finalpaths , 'shortroute': shortroute})


@app.route('/BFS')
def bfs():
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

    g.generatePaths(1,11)
    shortroute = TSPSol.modlist(g.finalpaths, totalpoints, coordslist)
    return jsonify({ 'routes': g.finalpaths,'shortroute': shortroute})


app.run(port= 5001)
