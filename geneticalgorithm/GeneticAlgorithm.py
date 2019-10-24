
import random
import operator
import time
import math
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from TSPSol import dist,load,plotgraph
from progress.bar import Bar
totalpoints,coordslist=load('../Random222.tsp')
totalpointsInt = int(totalpoints)



# A list to store the population i.e the list of routes in this problem statement



#This is to print all the routes from the list of routes in a more readable fashion
def printRoute(listofRoutes):
    for idx,route in enumerate(listofRoutes):
        print("Route: %d, Length of Route: %d,Distance of Route: %d, Fitness of route: %f \n %s"%(idx,len(route),distanceofRoute(route),calcfitness(route),route))


#Function to return of a given route
def distanceofRoute(route):
    distance =0

    #print("Distance calculated for the route",route)
    for index in range(0,len(route)-1):
        distance=distance+dist(route[index],route[index+1],coordslist)

    distance=distance+dist(route[0],route[99],coordslist)
    return distance

# This function is to return a random individual route from the list of input cities
def createroute():
    cityList = list(range(1, totalpointsInt + 1))
    return random.sample(cityList,len(cityList))


#This function is to return population(size based on given input) of routes
def createPopulation(popsize):
    population=[]
    i=0
    while i < popsize:
        population.append(createroute())
        i+=1
    return population


#This function is to return the fitness of each individual route
def calcfitness(route):
    distance=distanceofRoute(route)
    return (1/distance)*100000




#print(population)
#This function is to return a dictionary { 'population index' : ' fitness value' } sorted on fitness results
def rankroutes(population):
    fitnessresults={}
    for idx,route in enumerate(population):
        fitnessresults[idx]=calcfitness(route)

    return sorted(fitnessresults.items(),key=operator.itemgetter(1),reverse=True)



#rankedPop = rankroutes(population)
#print("ranked pop: ",rankedPop)


# This function is to return parents route id's (based on input size) based on their fitness ranking
def selection(rankedpop,size):
    selectedParents =[]

    for i in range(0,size):
        selectedParents.append(rankedpop[i][0])

    for i in range(size,len(rankedpop)):

        selectedParents.append(rankedpop[i][0])


    return selectedParents

#selectedParents = selection(rankedPop,20)
#print("selectedParents",selectedParents)


# This function is to return the mating pool (list of parent routes)to generate next generation
def matingPool(population,selectedParents):
    matingPool=[]
    for index in selectedParents:
        matingPool.append(population[index])

    return matingPool


#matingPool= matingPool(population,selectedParents)

#print("Parent1 : No of cities: %d \n %s"%(len(matingPool[0]),matingPool[0]))
#print("Parent2 : No of cities: %d \n %s"%(len(matingPool[1]),matingPool[1]))



# This function returns a child by performing ordered cross over between parent 1 and 2 from the mating pool
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    #Picking a random city index in the route of parent 1
    geneA = int(random.random() * len(parent1))

    #Picking a random city in the route of parent 2
    geneB = int(random.random() * len(parent1))
    #print("Gene A: %d Gene B: %d"%(geneA,geneB))

    #The starting index from where the cities would be inherited from the parent1 by the child
    startGene = min(geneA, geneB)
    #The end of index from where the cities would be inherited from the parent1 by the child
    endGene = max(geneA, geneB)

    #print("StartGene: %d, EndGene: %d"%(startGene,endGene))


    #Retaining the parent 1 gene from this logic
    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    #print("ChildP1: ",childP1)


    #Rest of the cities would be picked from parent2 and since this is an ordered cross over function you need to pick cities that are not picked already and avoid duplicates
    childP2 = [item for item in parent2 if item not in childP1]

    #print("ChildP2: ",childP2)

    # Appending cities from parent1 and parent2 to form the final child route
    child = childP1 + childP2
    return child



# This function returns a child by performing ordered cross over between parent 1 and 2 from the mating pool
def breed2(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    #Picking a random city index in the route of parent 1


    #Picking a random city in the route of parent 2

    #print("Gene A: %d Gene B: %d"%(geneA,geneB))

    #The starting index from where the cities would be inherited from the parent1 by the child
    startGene = 2
    #The end of index from where the cities would be inherited from the parent1 by the child
    endGene = math.floor(len(parent1)*0.25)

    #print("StartGene: %d, EndGene: %d"%(startGene,endGene))


    #Retaining the parent 1 gene from this logic
    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    #print("ChildP1: ",childP1)


    #Rest of the cities would be picked from parent2 and since this is an ordered cross over function you need to pick cities that are not picked already and avoid duplicates
    childP2 = [item for item in parent2 if item not in childP1]

    #print("ChildP2: ",childP2)

    # Appending cities from parent1 and parent2 to form the final child route
    child = childP1 + childP2
    return child




def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def breedPopulation2(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed2(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children




#print("Next Generation children: %d \n %s"%(len(children),children))



#Swap Mutation is followed as we need to abide by the rules for TSP i.e all the cities should be retained and shouldn't be duplicated
#Mutate function would take route and the rate of mutation required as an argument
def mutate(route, mutationRate):
    for swapped in range(len(route)):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * len(route))
            #print("Swapping happening ")
            city1 = route[swapped]
            city2 = route[swapWith]

            route[swapped] = city2
            route[swapWith] = city1
    return route


#Mutate population would take the population as input and loop though the mutate function to generate all new childs
def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop





def nextGeneration(currentGeneration,elitesize,mutationRate):

    #print("CurrentGeneration Size: %d \n"%len(currentGeneration))
    #Rank the current population based on fitness
    rankedCurrentGen = rankroutes(currentGeneration)

    #Select the top n(of input size) parents based on fitness results
    selectParentIds= selection(rankedCurrentGen,elitesize)

    #Find the list of actual parent routes from their ID's
    matingParents= matingPool(currentGeneration,selectParentIds)


    #From the mating parents it will return childrens list of routes of size given in input
    childrenPop=breedPopulation(matingParents,elitesize)

    #The children are futher mutated to create a next generatiomn of population
    nextGeneration=mutatePopulation(childrenPop,mutationRate)

    return nextGeneration


def geneticAlgorithm(popsize,elitesize,mutationRate,generations):
    progress=[]



    #Returns a random population of routes[1..100]
    #No of routes returned is based on input size (popsize)
    pop = createPopulation(popsize)

    #printRoute(pop)

    print(rankroutes(pop))
    print("Initial distance of the top route in the generation: " + str(distanceofRoute(pop[rankroutes(pop)[0][0]])))

    for i in range(0, generations):
        sys.stdout.write("\rGeneration %i"%i)
        sys.stdout.flush()
        #print("Generations",i)

        pop = nextGeneration(pop,elitesize, mutationRate)
        shortestDistofGen = distanceofRoute(pop[rankroutes(pop)[0][0]])
        progress.append(shortestDistofGen)
        if(shortestDistofGen < 1600):
            print("Total distance of the below route is less than 1000 : Found route in Generation %d"%i)
            bestRouteIndex = rankroutes(pop)[0][0]
            bestRoute = pop[bestRouteIndex]
            print(bestRoute)
            print("Distance: ",shortestDistofGen)
            break;



    #print("Final distance of the top route in the generation: " + str(distanceofRoute(pop[rankroutes(pop)[0][0]])))
    timeinseconds = (time.time() - start_time)/60
    print("--- %d minutes taken to execute the program---" % timeinseconds)
    bestRouteIndex = rankroutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    bestRoute.append(bestRoute[0])
    plotgraph(len(progress),coordslist,bestRoute)

    plt.plot(progress)
    plt.ylabel('Cost')
    plt.xlabel('Generation')
    plt.show()

    return bestRoute


#drawroute =[1, 71, 24, 89, 7, 36, 37, 38, 66, 21, 3, 41, 39, 53, 19, 91, 63, 32, 28, 61, 55, 46, 34, 86, 23, 96, 100, 45, 52, 22, 67, 27, 9, 82, 57, 44, 80, 58, 5, 42, 62, 50, 14, 76, 2, 48, 65, 88, 78, 26, 77, 87, 49, 11, 16, 70, 94, 75, 74, 17, 93, 99, 69, 47, 12, 18, 35, 4, 59, 33, 64, 31, 84, 40, 6, 20, 81, 98, 60, 25, 13, 56, 29, 97, 51, 8, 54, 90, 10, 83, 85, 72, 30, 73, 95, 15, 79, 68, 43, 92,1]

#plotgraph(coordslist,drawroute)





start_time = time.time()

    # First Argument -- number of routes in a population
    # Second Argument -- Elite Size to retain (how much of the top poulation are to be retained for next generation)
    # MutationRate -- Rate of Mutation
    # Fourth Argument -- How many generations the program can run?
bestRoute = geneticAlgorithm(100, 30, 0.0003, 100000)

print(distanceofRoute(bestRoute))



