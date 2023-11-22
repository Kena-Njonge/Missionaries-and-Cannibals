import networkx as nx
import matplotlib.pyplot as plt

i = 0
j = 0
stateList = []

while i < 4:
    for j in range(4):
        stateList.append((i, j))
    i += 1

G = nx.Graph()

stateListTuple = tuple(stateList)

for j in stateListTuple:
    G.add_node(j)

for j in stateListTuple:
    for k in stateListTuple:
        if j[0] == (k[0] + 1) and j[1] <= (k[1] + 1):
            G.add_edge(j, k)
        elif j[1] == (k[1] + 1) and j[0] <= (k[0] + 1):
            G.add_edge(j, k)
        elif j[0] == (k[0] + 2) and j[1] == k[1]:
            G.add_edge(j, k)
        elif j[1] == (k[1] + 2) and j[0] == k[0]:
            G.add_edge(j, k)

# Create an independent copy of the graph before pruning
G_pruned = G.copy()

# Identify nodes to be removed as to avoid runtime error related to removing nodes while searching for nodes to be removed
nodes_to_remove = [node for node in G_pruned.nodes() if node[0] < node[1]]

# Remove nodes
for node in nodes_to_remove:
    G_pruned.remove_node(node)

# Draw the pruned graph
nx.draw(G_pruned, with_labels=True, font_weight='bold')


# Save the graph as an image (PNG format in this example)
plt.savefig("output_graph.png")

# Show the plot
plt.show()


