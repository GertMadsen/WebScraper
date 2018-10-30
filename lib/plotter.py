import networkx as nx
import matplotlib.pyplot as plt
import os

def make_graph(url_dict, plot_file):
    # plot_data = []   
    # for key, values in url_dict.items():
    #     for value in values:
    #         plot_data.append((key,value,1))      
    
    # DG = nx.DiGraph()
    # DG.add_weighted_edges_from(plot_data)
    
    DG = nx.DiGraph(url_dict, rank="source")
    options = {
      'with_labels': False,  
      'node_color': 'black',
      'edge_color': 'grey',
      'node_size': 2,
      'width': 0.1,     
      'arrows': True,
      'arrowsize' : 5,
    }
    nx.draw(DG, **options)

    plot_dir = 'plots'
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()