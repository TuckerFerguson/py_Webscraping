#@author Tucker Ferguson
#1/30/2020
#
# Step 1) Utilizing urllib3/BeautifulSoup I access a web address, extract its html, parse using bs4.
#
# Step 2) Using regular expressions (re) to extract scores
from datetime import datetime
from bs4 import BeautifulSoup
import urllib3
import re

theDate = ""

longDate = str(datetime.today())
longDate = longDate.split(" ")
theDate = longDate[0]
theDate = theDate.split("-")
urlOrder = theDate[1] + "/" + theDate[2] + "/" + theDate[0]


url = "https://stats.nba.com/scores/"+urlOrder

print(url)
html_Pool = urllib3.PoolManager()
content = html_Pool.request('GET',url)
soup_Content = BeautifulSoup(content.data,'html.parser')

results = soup_Content.find_all("table")
print(results)