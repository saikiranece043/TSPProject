#This is a class to represent a city that has 2 properties x,y

class City:

    #Constructor to set the x and y coordinates of the city
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #Function to calculate distance to another city given it's object
    def distance(self,city):

        distance =0
        return distance

    def __repr__(self):
        return "(" + str(self.x)+","+str(self.y)+")"


