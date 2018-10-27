import re
import bs4
import requests
from tqdm import tqdm


def scrape_starter(url, depth):
    print('Scraping from: {}'.format(url))
    print('Scraping to depth: {}'.format(depth))
    return scrape_links(url, depth)

def scrape_links(from_url, depth, for_depth=0, all_links={}):
    try:
        r = requests.get(from_url, timeout=5)
        r.raise_for_status()
        soup = bs4.BeautifulSoup(r.text, 'html5lib')
        raw_list = [a['href'] for a in soup.find_all('a', href=True)]
        url_list =[url for url in raw_list if url.startswith('http')] 
        all_links.update({from_url: url_list}) 
        for_depth += 1
        if for_depth < depth:           
            for url in tqdm(url_list):
                 if (url not in all_links): 
                     scrape_links(url, depth, for_depth, all_links)                    
    except:
        pass
    return all_links