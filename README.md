# TSPProject
This is a project to solve Traveling Salesman Problem

The project has so far solved the travelsman Sales Problem in different ways for different types of input data

# Brute Force method.
  This method is to find the cost of the tour for all the possible paths.
  This method can be used only to solve when there is limited number of input cities and the time complexity is O(n!).
  TSPSol.py is the python file which solves this problem

# Depth First Search
  The problem is approached with given set of limitations of how each city (node) in the path could be traversed.
  Based on the restriction all the possible tours are traversed using DFS and shortest among them is displayed as output
  DFS.py is the python file which solves this problem
  
# Breadth First Search 
  The problem is approached with given set of limitations of how each city (node) in the path could be traversed.
  Based on the restriction all the possible tours are traversed using DFS and shortest among them is displayed as output
  BFSCl.py is the python file which solves this problem

# Greedy Algorithm 
   The greedy algorithm works with more number of data inputS i.e nearly 40 cities or even more on the tour.
   The performance of the algorithm is swift however it doesn't provide you the globally optimal solution
   Greedy.py is the python file which solves the problem


# Genetic Algorithm 
   Genetic Algorithm is implemented to solve the TSP problem with 100 cities. This algorithm would create a random initial population and create next generations based on the fitness of the inital population. 
The results of this algorithm is better than greedy approach. However this approach would consume resources considerably as we need to search for an optimal solution through mutiple generations. We wouldn't be able to tell how many generations it would take to find globally optimal solution, in some cases you may never find it. So it wouldn't always gurantee you globally optimal solution but still get a nearly optimal solution
    
# Genetic Algorith with Wisdom of Crowds
   This is an extension to genetic algorithm. Implement the idea of wisdom of crowds where research states that a solution generated from a group of people would be better than the solution developed by a smartest individual in the group. Inspired from this idea we would observe how our genetic algortithm would respond to this approach. It's expected to give better results and we would experiment the same.
