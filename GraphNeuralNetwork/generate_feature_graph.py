import networkx as nx
import  pandas as pd
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

eigenvector_centrality = nx.eigenvector_centrality(G)

katz_centrality = nx.katz_centrality(G)


harmonic_centrality = nx.harmonic_centrality(G)


clustering_coefficient = nx.clustering(G)


shortest_path_lengths = nx.average_shortest_path_length(G)


density = nx.density(G)


assortativity = nx.degree_assortativity_coefficient(G)


edge_betweenness = nx.edge_betweenness_centrality(G)
edge_load = nx.edge_load(G)

structural_holes = nx.constraint(G)


# Create a dictionary with features
features_dict = {
    'node_id': list(G.nodes),
    'degree_centrality': list(degree_centrality.values()),
    'betweenness_centrality': list(betweenness_centrality.values()),
    'closeness_centrality': list(closeness_centrality.values()),
    'eigenvector_centrality': list(eigenvector_centrality.values()),
    'katz_centrality': list(katz_centrality.values()),
    'harmonic_centrality': list(harmonic_centrality.values()),
    'clustering_coefficient': list(clustering_coefficient.values()),
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(features_dict)

# Print the DataFrame
print(df)




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

