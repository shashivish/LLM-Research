import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.DiGraph()

# Add edges to the graph
edges = [('A', 'B'), ('B', 'C'), ('E', 'F')]
G.add_edges_from(edges)

G_undirected = nx.Graph()

# Add edges to the graph
G_undirected.add_edges_from(edges)

# Find connected components in the undirected graph
subgraphs_undirected = [G_undirected.subgraph(c).copy() for c in nx.connected_components(G_undirected)]

# Create a figure with subplots based on the number of subgraphs
n_subgraphs_undirected = len(subgraphs_undirected)
fig, axs = plt.subplots(1, n_subgraphs_undirected, figsize=(6 * n_subgraphs_undirected, 6))

# Check if there is only one subplot (i.e., one subgraph)
if n_subgraphs_undirected == 1:
    axs = [axs]

# Draw each subgraph with edge labels in a separate subplot
for i, sg in enumerate(subgraphs_undirected):
    pos = nx.spring_layout(sg)  # Define a layout for nodes
    nx.draw(sg, pos, with_labels=True, node_color='lightblue', edge_color='black', ax=axs[i])
    nx.draw_networkx_edge_labels(sg, pos, edge_labels={(u, v): f'{u} - {v}' for u, v in sg.edges()}, ax=axs[i])
    axs[i].set_title(f'Subgraph {i+1}')

plt.tight_layout()
plt.show()
