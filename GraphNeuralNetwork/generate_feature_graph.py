import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph

# Calculate Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Calculate Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Calculate Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)

# Calculate PageRank
pagerank = nx.pagerank(G)

# Perform Community Detection
communities = nx.community.greedy_modularity_communities(G)


communities = nx.community.greedy_modularity_communities(G)

# Access node attributes
node_attributes = G.nodes(data=True)

# Access edge attributes
edge_attributes = G.edges(data=True)

# More properties and features can be calculated based on your use case

# Access node attributes
node_attributes = G.nodes(data=True)

# Perform graph motif analysis
motifs = nx.algorithms.isomorphism.vf2_subgraph_isomorphisms(G, motif)

from sklearn.cluster import KMeans
import numpy as np

# Assuming you have node embeddings
node_embeddings = [...]  # List of node embeddings

# Convert embeddings to a numpy array
embedding_matrix = np.array(node_embeddings)

# Apply K-Means clustering
num_clusters = 3  # You can set the number of clusters
kmeans = KMeans(n_clusters=num_clusters)
clusters = kmeans.fit_predict(embedding_matrix)

# Assign cluster labels to nodes
node_clusters = {}  # Dictionary to store node_id : cluster_label
for i, node_id in enumerate(nodes):
    node_clusters[node_id] = clusters[i]

# Print the cluster assignments
for node_id, cluster_label in node_clusters.items():
    print(f"Node {node_id} belongs to cluster {cluster_label}")

