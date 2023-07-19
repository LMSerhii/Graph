import matplotlib.pyplot as plt

import networkx as nx

G = nx.DiGraph()

G.add_edge(1, 2, weight=1)
G.add_edge(1, 5, weight=1)
G.add_edge(1, 6, weight=1)
G.add_edge(1, 7, weight=1)
G.add_edge(7, 8, weight=1)


G.add_edge(2, 3, weight=1)
G.add_edge(2, 8, weight=1)
G.add_edge(2, 9, weight=1)
G.add_edge(2, 10, weight=1)
G.add_edge(8, 11, weight=1)


G.add_edge(3, 4, weight=1)
G.add_edge(3, 11, weight=1)
G.add_edge(3, 12, weight=1)
G.add_edge(3, 13, weight=1)
G.add_edge(11, 14, weight=1)


G.add_edge(4, 1, weight=1)
G.add_edge(4, 14, weight=1)
G.add_edge(4, 15, weight=1)
G.add_edge(4, 16, weight=1)
G.add_edge(16, 7, weight=1)


nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.show()