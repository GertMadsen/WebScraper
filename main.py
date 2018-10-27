'''
Usage: 
    python main.py <url> <depth>
Example:
   python webscrape.py https://www.dr.dk/ 3
'''

import lib.scraper as webscraper
import lib.plotter as plotter
import lib.filewriter as writer
import sys

if __name__ == '__main__':
    # url = 'https://pythoniter.appspot.com/?fbclid=IwAR2Kwxu7QKANwVBk82XP8FL85QvSCLe9dmzk-w78OxnHyU7qChsZxsCPhys'
    # url = 'https://www.dr.dk/'
    # url = 'http://www.pyregex.com/'
      
    try:
        _, url, depth = sys.argv   
        result = webscraper.scrape_starter(url, int(depth))
        writer.write_to_file(result)

        plotter.make_graph(result)

    except Exception as e:
        print(__doc__)
        sys.exit(1)  