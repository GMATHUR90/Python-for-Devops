#Graph: is a non linear data structure, it has vertices and edge
#Vertices: Nodes
#Edges: Connecting two nodes

import pprint #pprint(pretty printing python dsa) make easier to read and understand
class Vertex:
    def __init__(self,name):
        self.name = name
        self.connections = [] #connection here is like vertices1 to vertices2 or 
        #                      v1 connected to v4

    def add_edge(self,obj): #Adds a connection to another vertex
        self.connections.append(obj)#obj is another vertex that is current vertex 
                                    #connected to

class Edge: #Represent a connection between two vertices, indicating a relationship
    def __init__(self):
        self.connections = []#A list to store connection information(not used for graph
                             # representation in this code)

    def add_edge(self, from_vertices, to_vertices):#Add connections data(not directly used 
                                                   #for graph building)
        self.connections.append(from_vertices.name)
        self.connections.append(to_vertices.name)

class Graph: #Represent the overall graph structure, containing vertices and their connection
    def __init__(self):
        self.graph = {}#graph is a dictionary to store vertices and their connections

    def add_vertices(self,obj): #Add vetex to graph
        self.graph.update({obj.name:obj.connections})

V1 = Vertex("1")
V2 = Vertex("2")
V3 = Vertex("3")
V4 = Vertex("4")

e1 = Edge()
e1.add_edge(V1,V2)

e2 = Edge()
e2.add_edge(V1,V3)

e3 = Edge()
e3.add_edge(V2,V3)

e4 = Edge()
e4.add_edge(V3,V4)

e5 = Edge()
e5.add_edge(V4,V1)

#V1

V1.add_edge(e1.connections)
V1.add_edge(e2.connections)

#V2
V2.add_edge(e3.connections)

#V3
V3.add_edge(e4.connections)

#V4
V4.add_edge(e5.connections)


g1 = Graph()
g1.add_vertices(V1)
g1.add_vertices(V2)
g1.add_vertices(V3)
g1.add_vertices(V4)

pprint.pprint(g1.graph)

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Data_Structure_Graph.py"
{'1': [['1', '2'], ['1', '3']],
 '2': [['2', '3']],
 '3': [['3', '4']],
 '4': [['4', '1']]}
"""


#Modified Version of Graph

import pprint  # pprint for pretty-printing the graph

class Vertex:
    def __init__(self, name):
        self.name = name
        self.connections = []  # List to store connections to other vertices

    def add_edge(self, vertex):
        self.connections.append(vertex)  # Add a vertex to the connections list

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store vertices and their connections

    def add_vertex(self, vertex):
        self.graph[vertex.name] = [v.name for v in vertex.connections]  # Add vertex to the graph

# Create vertices
V1 = Vertex("1")
V2 = Vertex("2")
V3 = Vertex("3")
V4 = Vertex("4")

# Add edges (connections) between vertices
V1.add_edge(V2)  # V1 -> V2
V1.add_edge(V3)  # V1 -> V3
V2.add_edge(V3)  # V2 -> V3
V3.add_edge(V4)  # V3 -> V4
V4.add_edge(V1)  # V4 -> V1

# Create the graph and add vertices to it
g1 = Graph()
g1.add_vertex(V1)
g1.add_vertex(V2)
g1.add_vertex(V3)
g1.add_vertex(V4)

# Pretty-print the graph
pprint.pprint(g1.graph)

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Data_Structure_Graph.py"
{'1': ['2', '3'], '2': ['3'], '3': ['4'], '4': ['1']}
"""
