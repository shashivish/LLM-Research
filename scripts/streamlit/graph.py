import streamlit as st
import graphviz

# Create a Graphviz dot object
dot = graphviz.Digraph(format='png')

# Add nodes and edges
dot.node('A')
dot.node('B')
dot.node('C')
dot.edge('A', 'B', label='has')

# Create expand/collapse buttons
expand_a = st.button('Expand A')
expand_b = st.button('Expand B')

# Display the Graphviz graph using Streamlit
st.graphviz_chart(dot)

# Show details if buttons are clicked
if expand_a:
    st.write("Details of Node A:")
    # Add more information about Node A here
if expand_b:
    st.write("Details of Node B:")
    # Add more information about Node B here
