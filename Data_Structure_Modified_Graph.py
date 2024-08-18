import pprint

class Vertex:
    def __init__(self, name):
        self.name = name
        self.out_edges = []  # List to store outgoing edges (directed connections)

    def add_edge(self, vertex):
        self.out_edges.append(vertex)

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store vertices and their outgoing edges

    def add_vertex(self, vertex):
        self.graph[vertex.name] = vertex.out_edges

    def print_graph(self):
        pprint.pprint(self.graph)

# Create vertices
V1 = Vertex("1")
V2 = Vertex("2")
V3 = Vertex("3")
V4 = Vertex("4")

# Get user input for directed connections
while True:
    from_vertex = input("Enter the starting vertex (or 'done' to finish): ")
    if from_vertex.lower() == "done":
        break

    to_vertex = input("Enter the ending vertex for this connection: ")

    # Error handling for invalid vertex names
    if from_vertex not in [V1.name, V2.name, V3.name, V4.name] or to_vertex not in [V1.name, V2.name, V3.name, V4.name]:
        print("Invalid vertex name. Please enter a valid vertex name from 1, 2, 3, or 4.")
        continue

    # Add directed connection based on user input
    V1.add_edge(eval(from_vertex))  # Assuming user enters vertex names (e.g., V1.add_edge(V2))

# Create graph object
g1 = Graph()

# Add vertices to the graph
g1.add_vertex(V1)
g1.add_vertex(V2)
g1.add_vertex(V3)
g1.add_vertex(V4)

# Print the directed graph
print("\nDirected Graph:")
g1.print_graph()
