import networkx as nx
import pandas as pd

# Create a directed multigraph (replace this with your existing graph)
G = nx.MultiDiGraph()

# Add nodes and edges with transaction weights (replace this with your data)
G.add_edge('NodeA', 'NodeB', weight=100)
G.add_edge('NodeA', 'NodeC', weight=50)
# Add more nodes and edges as needed...

# Initialize dictionaries to store node properties
in_degree = {}
out_degree = {}
total_transaction_volume = {}
average_transaction_amount = {}
betweenness_centrality = {}
closeness_centrality = {}
community_membership = {}
unique_counterparties = {}

# Iterate through nodes to calculate properties
for node in G.nodes():
    # In-degree and Out-degree
    in_degree[node] = G.in_degree(node)
    out_degree[node] = G.out_degree(node)

    # Transaction volume and Average transaction amount
    in_weights = [data['weight'] for _, _, data in G.in_edges(node, data=True)]
    out_weights = [data['weight'] for _, _, data in G.out_edges(node, data=True)]

    total_transaction_volume[node] = sum(in_weights) + sum(out_weights)
    if in_degree[node] + out_degree[node] > 0:
        average_transaction_amount[node] = total_transaction_volume[node] / (in_degree[node] + out_degree[node])
    else:
        average_transaction_amount[node] = 0  # Handle division by zero

    # Betweenness Centrality and Closeness Centrality
    betweenness_centrality[node] = nx.betweenness_centrality(G, weight='weight')[node]
    closeness_centrality[node] = nx.closeness_centrality(G, distance='weight')[node]

    # Community Membership (you may use your preferred community detection algorithm)
    community_membership[node] = 0  # Replace with your community detection result

    # Number of Unique Counterparties
    unique_counterparties[node] = len(set(G.successors(node)))

# Create a DataFrame from the dictionaries
data = {
    'Node': list(G.nodes()),
    'In-Degree': list(in_degree.values()),
    'Out-Degree': list(out_degree.values()),
    'Total Transaction Volume': list(total_transaction_volume.values()),
    'Average Transaction Amount': list(average_transaction_amount.values()),
    'Betweenness Centrality': list(betweenness_centrality.values()),
    'Closeness Centrality': list(closeness_centrality.values()),
    'Community Membership': list(community_membership.values()),
    'Unique Counterparties': list(unique_counterparties.values())
}

df = pd.DataFrame(data)

print(df)
# Save the DataFrame to a CSV file
#df.to_csv('node_properties.csv', index=False)
