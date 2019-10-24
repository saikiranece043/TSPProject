#This class is to calculate a fitness of an individual path

class Fitness:


    def __init__(self,route):
        self.route = route
        self.distance = 0
        self.fitness =0

    #Calculate the total distance of the route
    def calDistanceRoute(self):
        totaldistance = 0
        return self.distance

    #Calcualte the fitness of the route based on the total distance of the routegit
    def calFitness(self):
        fitness=1/self.distance
        return fitness

    def __repr__(self):
        return "( Route: %s"%(self.route)+" ,Fitness of route: "+str(self.fitness)+ " ,Distance of route: "+str(self.distance)+")"
