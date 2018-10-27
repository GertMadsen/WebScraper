import networkx as nx
import matplotlib.pyplot as plt

def make_graph(url_dict):

    plot_data = []   
    for key, values in url_dict.items():
        for value in values:
            plot_data.append((key,value,1))      
    
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(plot_data)
    options = {
      'with_labels': False,  
      'node_color': 'black',
      'edge_color': 'grey',
      'node_size': 2,
      'width': 0.1,     
      'arrows': False,
    }
    nx.draw(DG, **options)
    plt.show()