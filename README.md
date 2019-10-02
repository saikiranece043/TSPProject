# TSPProject
This is a project to solve Traveling Salesman Problem

The project has so far solved the travelsman Sales Problem in 4 different ways for different types of input data

Brute Force method.
  This method is to find the cost of the tour for all the possible paths.
  This method can be used only to solve when there is limited number of input cities and the time complexity is O(n!)
  TSPSol.py is the python file which solves this problem

Using Depth First Search to traverse the shrotest path.
  The problem is approached with given set of limitations of how each city (node) in the path could be traversed
  Based on the restriction all the possible tours are traversed using DFS and shortest among them is displayed as output
  DFS.py is the python file which solves this problem
  
Using Breadth First Search to traverse the shortest path.
  The problem is approached with given set of limitations of how each city (node) in the path could be traversed
  Based on the restriction all the possible tours are traversed using DFS and shortest among them is displayed as output
  BFSCl.py is the python file which solves this problem

Greedy Algorithm to find a nearly optimal solution.
   The greedy algorithm works with more number of data inputS i.e nearly 40 cities or even more on the tour.
   The performance of the algorithm is quite however it doesn't provide you the globally optimal solution
   Greedy.py is the python file which solves the problem


Genetic Algorithm is used to find an optimal solution to the problem
    Genetic Algorithm is implemented to solve the TSP problem with 100 cities. This algorithm would create a random initial population and create next generations based on the fitness of the inital population. The results of this algorithm is better than greedy approach. However this approach would consume resources considerably as we need to search for an optimal solution through mutiple generations.
