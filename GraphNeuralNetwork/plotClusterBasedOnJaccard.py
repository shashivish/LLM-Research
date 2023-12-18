import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

# Create a graph
G = nx.Graph()

random.seed(100)

# Add nodes with random Jaccard similarity scores
for i in range(1, 11):
    for j in range(i+1, 11):
        jaccard_score = random.uniform(0, 1)
        G.add_edge(f'Node {i}', f'Node {j}', weight=jaccard_score)

# Use the spring layout to position nodes
positions = nx.spring_layout(G)

# Assign clusters based on Jaccard similarity
clusters = {}
cluster_id = 0
threshold =0.8

for node in G.nodes():
    # Check if the node has neighbors with Jaccard similarity above the threshold
    neighbors_above_threshold = [n for n, attr in G[node].items() if attr['weight'] >= threshold]

    is_existing_cluster_id_found = False
    if neighbors_above_threshold:
        # Assign All neighbours in same cluster
        for n in neighbors_above_threshold:
            if n in clusters:
                old_cluster_id =  clusters[n]
                is_existing_cluster_id_found = True
                break

        if is_existing_cluster_id_found:
            for n in neighbors_above_threshold:
                clusters[n] = old_cluster_id
        else:
            for n in neighbors_above_threshold:
                clusters[n] = cluster_id # Use old Cluster ID

    else:
        clusters[node] = cluster_id
    print(neighbors_above_threshold)
    print(clusters)
    cluster_id +=1

# Use the spring layout to position nodes based on Jaccard similarity
positions = nx.spring_layout(G, weight='weight')

# Draw the network with nodes colored by their cluster
plt.figure(figsize=(12, 12))

# Get a unique color for each cluster
unique_clusters = set(clusters.values())
colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_clusters)))

for cluster, color in zip(unique_clusters, colors):
    # Get the nodes in this cluster
    clustered_nodes = [node for node, cid in clusters.items() if cid == cluster]
    # Draw these nodes
    nx.draw_networkx_nodes(G, positions, nodelist=clustered_nodes, node_color=[color], label=f'Cluster {cluster}')

# Draw edges and labels
nx.draw_networkx_edges(G, positions, alpha=0.5)
nx.draw_networkx_labels(G, positions)

# Show the plot
plt.title("Network Visualization with Jaccard-based Clustering")
plt.axis('off')  # Hide the axes
plt.legend()
plt.show()
