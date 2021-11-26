# Amazon price tracker
This project aims to start with a list of Amazon UK product URLs and returns price change data to the user. 

An API for Amazon UK products was considered, but required either an advertising developer account or was not available freely. 
Therefore a webscraping method was developed instead using BeautifulSoup. 

## Web-scraping price data
We will be using Scrapy for working with Xpaths from the Amazon website to extract the price, title and other data. 

The [installation documentation](https://docs.scrapy.org/en/latest/intro/install.html#intro-install) mentioned that a virtual environment is recommended before installing Scrapy, so this was created first by running the following in the root directory of the project: 
`python -m venv price_tracker_env`
This created a folder within Amazon-Price-Tracker
