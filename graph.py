"""
This module defines a Graph class that represents an undirected graph. The Graph class contains 
methods to add nodes and edges, check if two nodes are neighbors, print all edges, get a node by 
its ID, get all node IDs, and perform depth-first and breadth-first searches. The Graph class uses 
the Node class, which is defined in a separate module, to represent nodes in the graph. Each node 
has an ID, data, and a dictionary of connected nodes. The main function at the end of the module 
creates a graph and adds six nodes to it.
"""


from node import Node


class Graph:
    total_V = 0

    def __init__(self):
        self.all_nodes = dict()

    def add_node(self, idx):
        if idx in self.all_nodes:
            return None
        Graph.total_V += 1
        new_node = Node(idx=idx)
        self.all_nodes[idx] = new_node
        return new_node

    def add_edge(self, src, dst, wt=0):
        if src in self.all_nodes and dst in self.all_nodes:
            self.all_nodes[src].add_neighbour(self.all_nodes[dst], wt)
            self.all_nodes[dst].add_neighbour(self.all_nodes[src], wt)

    def is_neighbour(self, u, v):
        return u in self.all_nodes and v in self.all_nodes[u].get_connections()

    def get_all_nodes_ids(self):
        return self.all_nodes.keys()