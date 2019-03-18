# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:20:42 2019

@author: nrhaw
"""
import networkx as nx
import matplotlib.pyplot as plt

# y = [0,1,1,0]
# x = [1,1,2,2]
# blue filled rectangle
# plt.fill(x,y)

G = nx.DiGraph()
G.add_edges_from(
    [('X0', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'X1')]
)

node_color_map = {'X0': 0.25,
           'X1': 0.25,
          }
node_colors = [node_color_map.get(node, 0.25) for node in G.nodes()]

blue_edges = [('X0', 'A'), ('D', 'X1')]
black_edges = [edge for edge in G.edges() if edge not in blue_edges]

edge_colors = ['black' if not edge in blue_edges else 'blue'
                for edge in G.edges()]

# Need to create a layout when doing
# separate calls to draw nodes and edges
#pos = nx.spring_layout(G)
pos = nx.fruchterman_reingold_layout(G)

print("pos: ", pos)
print("pos type: ", type(pos))

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = 'lightblue', 
                       node_size = 500)

nx.draw_networkx_labels(G, pos)

#nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='b', arrows=True)
#nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)

nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=30)

plt.show()


