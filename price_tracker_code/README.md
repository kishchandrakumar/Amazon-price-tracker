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

If the virtual environment was saved in a different directory entirely and wasn't listed for selection, we could have actived it by editing the settings.json file as highlighted in (this video)[https://youtu.be/TSH4C1Zipcs?t=345] ('open workspace settings (JSON)' in Command Pallette -> add `"python.pythonPath": "ENVIRONMENT_DIRECTORY/PATH TO PYTHON APP"`).

When a git pull was initiated on a different computer, the virtual environment was not discoverable in VS code. Of course, only the virtual environment files were downloaded, but no actual installation has taken place yet on this computer.

It was later learned, (via this article)[https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde] that the virtual environment folder is traditionally called 'env', and should be set to be ignored by Git by running `echo 'price_tracker_env' > .gitignore` after initialising the git repo, followed by running `pip freeze > requirements.txt`. This text file creates a list of dependencies for our project. This is what will be pushed to Git instead of the files in the virtual environment itself. This is because we want users who pull from git to actually install the required packages and versions, instead of just pulling the files which aren't actually installed.

One thing to note when running `pip freeze` was that many unneeded packages were installed in the virtual environment that I creatd. The way I created this virtual environment was not a fresh install of python. But what did it actually do? (The documentation for virtualenv)[https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html] states that `virtualenv venv` creates a copy of python. But we don't want this.

# Problem 3: requirements.txt has many packages such as Numpy and Matplotlib. Therefore these are also being installed in the virtual environments.

#### I think the base installation contains these packages. I should go and clean this up so it's just python, maybe using pip uninstall, or installing a clean version of python

#### How do I know which is considered the base installation of python? Can this be changed?

# Problem 2: verify whether users should reinstall from requirements.txt every time they pull from Remote

# Problem 4: understand workspaces etc. in VS code

# Problem 5: Understand Git pull requests, rebasing, merging, conflicts etc.

# Start a medium blog post, which I can practically copy/paste this README onto it.

# Problem 6: How to set the python interpreter for jupyter notebook?

Running `pip list` shows all globally available site packages. This is what's being installed in our virtual environment as well, at this stage.
Remember last time I ran `python -m venv [NEW ENVIRONMENT NAME]`. If I instead run `virtual_env [NEW ENVIRONMENT NAME]` within the project's root directory, activate the environment by running `source [NEW ENVIRONMENT NAME]/bin/activate` then running `pip list`, we don't have many packages at all.
Running `python --version` gives us 3.8.2, whereas our base version is 2.7.9. So how is virtual_env selecting its python version?

Install scrapy into this virtual environment using `pip install scrapy` whilst the environment is activated. `pip list` should now only shows us packages related to scrapy (no Numpy or MatPlotLib).

We can now create a requirements.txt file with just the packages installed for this project `pip freeze --local > 'requirements.txt` whilst being inside the virtual environment. To double check, we can `deactivate` the environment and repeat the process `pip freeze --local > 'requirements_global.txt'` and observe that the 2 .txt files are different.

### determining the version of python to install in the virtual environment

We can also specify which version of python to install by pointing to a specific version of python installed on our system:
`virtualenv -p /usr/bin/python2.6 py26_env`
Note that it should already be installed prior to this line being able to run.

When on a new computer, we can set up a virtual environment, then run `pip install -r requirements.txt` to install the package dependencies on our system, followed by a `pip list` to double check installed packages.
