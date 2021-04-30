# BingBot
A program that performs automated searches on bing using Selenium to increase your Microsoft Rewards points.

# Requirements
You must install a chromedriver from ```https://sites.google.com/a/chromium.org/chromedriver/downloads``` and make sure it is the same version as your Google Chrome.
You could also install the geckodriver for Firefox instead.

Use pip to install the selenium package. Python 3.6 has pip available in the standard library. Using pip, you can install selenium like this:
```pip install selenium```

# Modifications
The PATH is set to where I saved my chromedriver in "C:\Program Files (x86)\chromedriver.exe", you can modify this to the location your chromedriver or geckodriver is saved.

Depending on your Microsodt account level you may want to modify the range in the for loop to increase or decrease the number of searches.
