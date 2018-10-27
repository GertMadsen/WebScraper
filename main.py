'''
Usage: 
    python main.py <url> <depth> <modulename>
Example:
   python main.py http://www.pyregex.com/ 3 pyregex
'''

import lib.scraper as webscraper
import lib.plotter as plotter
import sys
import pickle

if __name__ == '__main__':
      
    try:
        _, url, depth, module_name = sys.argv
        module_name += ".p"

        print('Starting webscrape.')   
        result = webscraper.scrape_starter(url, int(depth))
        print('Webscraping finished succesfully.')
        
        print('\nSaving result dictionary in a pickle module as: {}'.format(module_name))        
        try:
            pickle.dump( result, open( module_name, "wb" ))
            print('Pickle module was saved succesfully.')
        except Exception as e:
            print('Pickle module save failure!')

        print('\nCreating and viewing plot.')
        plotter.make_graph(result)
  
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

        