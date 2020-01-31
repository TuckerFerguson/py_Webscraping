#@author Tucker Ferguson
#1/29/2020
#
# Step 1) Utilizing urllib3/BeautifulSoup I access a web address, extract its html, parse using bs4.
#
# Step 2) Using regular expressions (re) to extract headlines

from bs4 import BeautifulSoup
import urllib3
import re

def headline(inputStr) :
    pass

myPool = urllib3.PoolManager()
content = myPool.request('GET','https://oldschool.runescape.com/')
souped_Content = BeautifulSoup(content.data,"html.parser")

pattern = r"\">\w.+</a"
newsInfo = souped_Content.find_all("a",class_="secondary-link")
outputList = []
for x in range(len(newsInfo) - 2):
    if x % 2 == 0: 
        output = re.search(pattern, str(newsInfo[x]))
        outputList.append(output.group(0))
formatter = []
for entries in outputList :        
    if '\">' in entries :
        entries = entries.replace('\">',"")
    if '</a' in entries :
        entries = entries.replace('</a',"")
    formatter.append(entries)

for i,x in enumerate(formatter) :
    print("News Article {}): {}".format(i+1,x))

