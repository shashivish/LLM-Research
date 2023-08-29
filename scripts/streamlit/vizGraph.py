import streamlit as st
import streamlit_visgraph as vg

# Create a graphviz object
graph = vg.DiGraph()

# Add some nodes to the graph
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

# Add some edges to the graph
graph.add_edge("A", "B")
graph.add_edge("B", "C")

# Customise the graph
st.visgraph(graph, node_size=200, edge_color="blue", node_label="text-align:center")