'''
Usage: 
    python main.py <url> <depth>
Example:
   python webscrape.py https://www.dr.dk/ 3
'''

import lib.scraper as webscraper
import lib.plotter as plotter
import sys
import pickle

if __name__ == '__main__':
    # url = 'https://pythoniter.appspot.com/?fbclid=IwAR2Kwxu7QKANwVBk82XP8FL85QvSCLe9dmzk-w78OxnHyU7qChsZxsCPhys'
    # url = 'https://www.dr.dk/'
    # url = 'http://www.pyregex.com/'
      
    try:
        _, url, depth = sys.argv
        pickle_module_name = 'webscrape.p'

        print('Starting webscrape.')   
        result = webscraper.scrape_starter(url, int(depth))
        print('Webscraping finished succesfully.')

        print('\nSaving pickle module as: {}'.format(pickle_module_name))
        try:
            pickle.dump( result, open( pickle_module_name, "wb" ))
            print('Pickle module was saved succesfully.')
        except Exception as e:
            print('Pickle module save failure!')

        print('\nCreating and viewing plot.')
        plotter.make_graph(result)
  
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

        