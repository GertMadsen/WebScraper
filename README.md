# Python Assignment 6
### WebScraper for scraping internet pages for http links.

* This program scrapes an internet page from a given url and subpages according to the depth alse given. 
* This program also produces a pickle module file with the scraped links and an plot that shows the connection between the scraped links.

### Procedure to run the program:
* Clone the project on your computer.
* How to use the program:
  * In a command prompt or bash with Python available, use the following command
  * python main.py \<url> \<depth> \<modulename>
   * \<url> - url to scrape
   * \<depth> - how deep to scrape
   * \<modulename> name to use for pickle module (.p will be added when module is created)
  * example: python main.py http://www.pyregex.com/ 3
  
### Warning:
* Large depth value will result in a long scraping runtime.
  

