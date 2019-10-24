import sys
import time
class Node:
    def __init__(self,data):
        self.left = ''
        self.right = ''
        self.data=data

    def __repr__(self):
        return "Node %s Left Node %s right Node: %s"%(str(self.data),str(self.left),str(self.right))

    def addNodetoNode(self,n):
        if(self.data > n.data):
            self.left =n
        elif(self.data < n.data):
            self.right= n


class Tree:
    def __init__(self):
        self.root = ''

    def addnode(self,val):
        node = Node(val)
        if (self.root == ''):
            self.root = node
        else:
            self.root.addNodetoNode(node)


    def __repr__(self):
        return "Tree Root Node: "+str(self.root)



#
# for i in range(12, 6, -1):
#     sys.stdout.write("\rDoing thing %i" % i)
#     sys.stdout.flush()
#     time.sleep(1)


order = [4,28,14,7,19,6,8]





def sorting(a):

    for j in range(1, len(a)):
        key = a[j]
        #print(key)
        i=j-1
        #print(a[j])
        while i> 0 and a[i] > key:

            a[i+1] = a[i]
            i=i-1

        a[i+1] = key

    print(a)

#sorting(order)



#write a program to calulate the number of multpication of matrices

#Input no of matrices i,j   spilt the matrices into i,k k+1,j

#(1,1) (2,10)


# def multiplicationsMatrices(i,j):
#     count =0
#     for k in range(i,j-1):
#          print("( %d, %d ) , ( %d , %d ) \n"%(i,k,k+1,j))
#          diff =  j - (k+1)
#
#          if( diff > 1):
#              multiplicationsMatrices(k+1,j)
#          count= count+1
#     return count
#
#
#
#
#
# print("Possible multipication combinations : ",multiplicationsMatrices(1,10))




# hash tables in python
# so you need to insert a key





##Types of data structures in python list tuple set and dict


## List
x =list()
y =tuple()
z= set()
a= dict()
print(type(a))
print(type(x))
print(type(y))
print(type(z))

# list is used to store data types of different data types

# there are lot of functions to play with lists starting with substring



#Create a list

newlist = [1,2,3,4]


matrix = [ [1,1] , [1,2] ]
# list[start,end] and other functions below to find max,min,check if item in the list,sum of all the elements in the list
#
print(newlist[1:3])
print(newlist[-1])

print(max(newlist))
print(min(newlist))
print(1 in newlist)
print(sum(newlist))
print()

# tuple is used to store list of data that is immutable ,however the list inside can change
# set is to store a set of unique items duplication not allowed
# dict is to store key and value pairs
# stack LIFO and queue FIFO is another implementation
# dequeue can be used to implement both
# linked list


# given a number of matrices and their dimensions cal the min number of multiplications order
# this is an example of dynamic programming

#bottom to top approach

# A1, A2, A3
# (5,2) (2,6) (6,4)

# Ci,j = Ai,k + Bk+1,j + di-1 * dk * dj


def mult(i,j):
    if (i == j ):
        return 0

    for k in range(i,j-1):
        return

# its all about time complexity and space complexity and what operations are better in what cases in grips
# so lets find out what's going on
# time complexity -- saikiran and saikiran saikiran and this is the best story of all time



count=0
x= [3,-2,1,4,7,1]
l= len(x)
counter=[]



def increseq(x,l):
    for i in range(0, l - 1):
        if(i!=0):
            counter.append(count+1)
        print("\nSequence starts ",x[i],end="")
        count = 0
        for j in range(i + 1, l - 1):

            if (x[i] < x[j]):
                print(",",x[j],end="")
                count = count+1
#increseq(x,l)

#print("\nMax sequence count:",max(counter))

z = 0

def func1(n):
    if n>1:
        func1(n-1)
    for i in range(0,n):
        print("*")


func1(5)


#Recursion requires a base case and a case where recursion should occur
# So you need to break the big problem into smaller problems


#for example delivering parcels to houses



houses = [ "saikiran", "sinisanakr", "sambamurty" , "andrew", "devisowj","vinod"]

def deliver(houses):
    if len(houses) == 1:
        print("delivering the parcel to",houses)

    else:
        mid = len(houses) // 2
        deliver(houses[:mid])
        deliver(houses[mid:])

deliver(houses)



#Advanced Databases -- data warehousing, relational databases (allowing datatypes of ), no sql databases,
#Distributed Systems Design
#Intro to Cryptography
#Data Mining with Linear Model


# how to solve the number of steps problem recursively
#increasing subsequence
A= [3,-2,1,4,7,1]

3


def LIC(a):
    n=len(a)
    x = [1] *n

    for i in range(0,n):
        for j in range(i+1,j):
            if a[i] < a[j]:
                x[j] = x[j]+1