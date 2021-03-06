# Python Assignment 6
### WebScraper for scraping internet pages for http links.

* This program scrapes an internet page from a given url and subpages according to the depth alse given. 
* This program also produces a pickle module file with the scraped links and a circular networkx DiGraph plot that shows the connection between the scraped links.

### Dependencies:
* Python - Anaconda Distribution 
  * *In order to make sure that all librabies are present for a problem free execution of the software, we recommend using an Anaconda distribution of Python. But the software will probably also run with other distributiions, but then libraries such as Requests might need to be installed.*
 
* Networkx
  * To install networkx via Anaconda use: conda install -c anaconda networkx 

### Procedure to run the program:
* Clone the project on your computer.
* How to use the program:
  * In a command prompt or bash with Python available, use the following command
  * python main.py \<url> \<depth> \<modulename>
   * \<url> - url to scrape
   * \<depth> - how deep to scrape
   * \<modulename> name to use for pickle module (.p will be added when module is created)
  * example: python main.py http://www.pyregex.com/ 3 pyregex
  
### Warning:
* Large depth value will result in a long scraping runtime.
* For testing use a depth less than 4 to ensure a short runtime.
  
### Plot example for http://www.dr.dk/ with a depth of 4:

![Plotting](https://github.com/GertMadsen/pictures/blob/master/dr_dk.png)
