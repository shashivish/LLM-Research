import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.DiGraph()

# Add edges to the graph
edges = [('A', 'B'), ('B', 'C'), ('E', 'F')]
G.add_edges_from(edges)

# Find connected components in the graph
# For a directed graph, we use weakly connected components
subgraphs = [G.subgraph(c).copy() for c in nx.weakly_connected_components(G)]

# Create a figure with subplots based on the number of subgraphs
n_subgraphs = len(subgraphs)
fig, axs = plt.subplots(1, n_subgraphs, figsize=(6 * n_subgraphs, 6))

# Check if there is only one subplot (i.e., one subgraph)
if n_subgraphs == 1:
    axs = [axs]

# Draw each subgraph in a separate subplot
for i, sg in enumerate(subgraphs):
    nx.draw(sg, with_labels=True, node_color='lightblue', edge_color='black', ax=axs[i])
    axs[i].set_title(f'Subgraph {i+1}')

plt.tight_layout()
plt.show()
