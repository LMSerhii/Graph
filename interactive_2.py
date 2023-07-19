from pyvis.network import Network
import pandas as pd
import networkx as nx

net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
net.add_nodes(
    [1, 2, 3, 4, 5],
    label=['Node#1', 'Node#2', 'Node#3', 'Node#4', 'Node#5'],
    title=['Main node', 'Just node', 'Just node', 'Just node', 'Node with self-loop'],
    color=['#d47415', '#22b512', '#42adf5', '#4a21b0', '#e627a3'],
)

net.add_edges([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 1), (4, 1)])
net.show('graph.html', notebook=False)

