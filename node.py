"""
This Node class represents a node in a graph. Each node has an identifier (id), data, and 
a dictionary of connections to other nodes. The 'addNeighbour' method is used to add a connection 
from this node to another ('neighbour'), with an optional weight. The 'setData' method is used to 
set the data of the node. The 'getConnections' method returns the keys of the 'connectedTo' dictionary, 
which are the ids of the nodes connected to this node. The 'getID' and 'getData' methods return the 
id and data of the node, respectively. The 'getWeight' method returns the weight of the connection to 
a given neighbour. The '__str__' method returns a string representation of the node, showing its data 
and the data of its connections.
"""


class Node:

    def __init__(self, idx, data=0):
        self.id = idx
        self.data = data
        self.connected_to = dict()

    def add_neighbour(self, neighbour , weight = 0) :
        if neighbour.id not in self.connected_to.keys() :  
            self.connected_to[neighbour.id] = weight

    def set_data(self, data) : 
        self.data = data 

    def get_connections(self) : 
        return self.connected_to.keys()

    def get_id(self) : 
        return self.id
    
    def get_data(self) : 
        return self.data

    def get_weight(self, neighbour):
        return self.connected_to[neighbour.id]

    def __str__(self):
        return str(self.data) + ' Connected to : ' + str([x.data for x in self.connected_to])