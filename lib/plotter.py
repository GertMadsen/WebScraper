import networkx as nx
import matplotlib.pyplot as plt

def make_graph(url_dict):
    DG = nx.DiGraph()
    options = {
      'with_labels': False,  
      'node_color': 'black',
      'edge_color': 'grey',
      'node_size': 2,     
      'arrows': False,
    }   
    for key, values in url_dict.items():
        for value in values:
            DG.add_edge(key, value) 

    nx.draw(DG, **options)
    plt.show()