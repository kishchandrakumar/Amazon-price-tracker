# Amazon price tracker
This project aims to start with a list of Amazon UK product URLs and returns price change data to the user. 

An API for Amazon UK products was considered, but required either an advertising developer account or was not available freely. 
Therefore a webscraping method was developed instead using BeautifulSoup. 

## Web-scraping price data
We will be using Scrapy for working with Xpaths from the Amazon website to extract the price, title and other data. 

The [installation documentation](https://docs.scrapy.org/en/latest/intro/install.html#intro-install) mentioned that a virtual environment is recommended before installing Scrapy, so this was created first by running the following in the root directory of the project: 
`python -m venv price_tracker_env`
This created a folder within Amazon-Price-Tracker called `price_tracker_env` and moving the code to a separate folder called `price_tracker_code`. It's important the env folder is not in the directory containing the code itself, or it will not be findable by VScode Python interpreter selector. 

Upon opening a new terminal window within VScode, the following error was thrown: "cannot be loaded because running scripts is disabled on this system". (This article)[https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl/67420296#67420296] contains an addition to settings.json which provides a solution. After restarting VSCode and opening a new terminal window, the environment was automatically activated. 

If the virtual environment was saved in a different directory entirely and wasn't listed for selection, we could have actived it by editing the settings.json file as highlighted in (this video)[https://www.youtube.com/watch?v=TSH4C1Zipcs&ab_channel=NathanLoop-NetworkAutomation] .
