'''
Usage: 
    python main.py <url> <depth> <modulename>
Example:
   python main.py http://www.pyregex.com/ 3 pyregex
'''

import lib.scraper as webscraper
import lib.plotter as plotter
import os
import sys
import pickle

if __name__ == '__main__':
      
    try:
        _, url, depth, module_name = sys.argv

        plot_file = module_name+".png"
        module_name += ".py"
        
        print('Starting webscrape.')   
        result = webscraper.scrape_starter(url, int(depth))
        print('Numbers of links pages scraped: {}'.format(len(result)))
        print('Webscraping finished succesfully.')
        
        # print('\nSaving result dictionary in a pickle module as: {}'.format(module_name))        
        # try:
        #     module_dir = 'pickle_modules'
        #     if not os.path.isdir(module_dir):
        #         os.makedirs(module_dir)
        #     with open(os.path.join(module_dir, module_name), "wb" ) as fp:
        #         pickle.dump( result, fp)
        #     print('Pickle module was saved succesfully.')
        # except Exception as e:
        #     print('Pickle module save failure!')

        print('\nSaving result dictionary in a python module as: {}'.format(module_name)) 
        try:
            module_txt = 'SCRAPED_LINKS = {}'.format(str(result))
            module_dir = 'modules'
            if not os.path.isdir(module_dir):
                os.makedirs(module_dir)
            with open(os.path.join(module_dir, module_name), "w" ) as fp:
                fp.write(module_txt)
        except Exception as e:
            print('Python module save failure!')        

        print('\nCreating and viewing plot.')
        plotter.make_graph(result, plot_file)
  
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

        