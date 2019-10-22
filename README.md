# Auto-Challenge-with-behave

python-cucumber features using Behave

## Python Setup

To manage different versions of Python install pyenv using homebrew

See [The right and wrong way to set Python 3 as default on a Mac](https://opensource.com/article/19/5/python-3-default-mac)

This example was written with python 3.7.4, "__init.py" files are not present
## Behave Setup

`$ pip install behave`

`$ pip install selenium`

Credentials can be added to the behave.ini file but the details not committed, these can then be accessed in the code via 
context.config.userdata.get(keyword) rather than via the command line. 

Ok as a demo but obviously needs to be more secure for a live site.